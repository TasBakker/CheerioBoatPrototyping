# Special thanks to Jackson Wilt, Nico Schramma & Vera Horjus for providing 
# code on which this notebook is based on.

import cv2
import numpy as np
import pims
import os
import trackpy as tp
import pandas as pd
import matplotlib.pyplot as plt
import warnings
from rich.progress import track
warnings.simplefilter(action='ignore', category=FutureWarning)
tp.quiet(True)

directory_path = r'Tracking_videos\6-5-2025_Luk' # De folder waar de videos in staan (dit neemt ook subfolders mee)
graphs_path = r'Tracking_plots' # De folders waar de plots in uitkomen
shorten = 1
reducefps = 6
colorthreshold = 0.25

filedata = []
velocitydata = []
filepaths = []

def list_files_recursive(path='.'):
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            list_files_recursive(full_path)
        else:
            filepaths.append(full_path)

list_files_recursive(directory_path)

print('files to process:')
for file in filepaths:
    print(file.split('\\')[-1])
print('\n')

def locate_dots(frames, shorten=1, reducefps=12, colorthreshold=0.3):
    positions= [] #lists to be filled with their respective frame types

    for i in track(range(0,int(len(frames)/shorten),reducefps),'Processing frames'):
        r,gr,b = cv2.split(frames[i]) # split the color image into different channels   
        # gr =  np.zeros_like(gr, np.uint8)
        blurthis = (abs((r/255)-(gr/255))+abs((gr/255)-(b/255))+abs((r/255)-(b/255))) # calculate the color difference for each pixel from 0-1 (this highlights pixels with a lot of a single color)

        blurthis[blurthis>=colorthreshold] = 255 # set color difference values above a threshold to max intensity
        blurthis[blurthis<colorthreshold] = 0 # set color difference values below the same threshold to zero intenisty
        blur = cv2.medianBlur(np.uint8(blurthis), ksize=9) # blur to help houghcircles. If all went well, only the colored dots on the cheerioboat remain.

        circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, dp=1.5, minDist=35, param1=60, param2=10, minRadius=4, maxRadius=20) # actually find the circles in the edited image  #60,10
        try: circles = np.uint16(np.around(circles)) # round the found circle positions and radii
        except: continue

        background = np.zeros_like(blur, np.uint8) # create a black greyscale background 
    
        for j in circles[0,:]:
            # draw the centers of the circles
            cv2.circle(background,(j[0],j[1]),3,(255,0,0),-1) 

        positions.append(background)

    f = tp.batch(positions, diameter=5, minmass=20, processes=1, invert=False)#37
    t = tp.link(f, search_range=120, memory=20, adaptive_stop=40)# WAS 90
        
    return t

for file in filepaths:
    filename = file.split('\\')[-1].removesuffix('.mp4')

    # if '60_deg_fins_1' not in filename: continue

    print(f'Starting: {file.split('\\')[-1]}')
    frames = pims.Video(file)
    duration = frames.duration

    if "6-5-2025_Luk" in file:
        frames = [frame[490: 1750, :] for frame in frames]
    t = locate_dots(frames, shorten, reducefps, colorthreshold)

    particles = list(set(t['particle']))
    framelist = list(set(t['frame']))

    # angular part
    theta = []
    for framenr in framelist:
        tt = t[t['frame'] == framenr]
        try: # calculate the angle of the particle with respect to an arbitrary axis
            dx = float((tt.loc[tt['particle'] == particles[1], ['x']]).iloc[0]) - float((tt.loc[tt['particle'] == particles[0], ['x']]).iloc[0])
            dy = float((tt.loc[tt['particle'] == particles[1], ['y']]).iloc[0]) - float((tt.loc[tt['particle'] == particles[0], ['y']]).iloc[0])
            theta.append(np.arctan(np.abs(dy/dx)))
        except: # if a frame does not have every particle, repeat the previous value
            try: theta.append(theta[-1])
            except: theta.append(0)

    omega = (np.insert(theta, 0, 0) - np.insert(theta, -1, 0))[1:-1] / (np.insert(framelist, 0, 0) - np.insert(framelist, -1, 0))[1:-1]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,5), constrained_layout=True)

    fig.suptitle(f'{filename}')

    ax1.plot(framelist, theta)
    ax1.set_title('Angle of the cheerioboat')
    ax1.set_xlabel('frame nr')
    ax1.set_ylabel('angle (radians)')
    ax1.set_xlim(min(framelist), max(framelist))
    ax1.set_ylim(0, np.pi / 2)

    ax2.plot(framelist[:-1], omega)
    ax2.set_title('Angular velocity of the cheerioboat')
    ax2.set_xlabel('frame nr')
    ax2.set_ylabel('angular velocity (radians/frame)')
    ax2.set_xlim(min(framelist), max(framelist))

    fig.savefig(f'{graphs_path}\\angular_data_{filename}.png', dpi=500,bbox_inches='tight')
    fig.clear()
    plt.clf()

    # velocity part
    # calculate the centre of the boat
    x = []
    y = []

    for framenr in framelist:
        try:
            x.append(sum(t.loc[t['frame'] == framenr]['x']) / len(t.loc[t['frame'] == framenr]['x']))
            y.append(sum(t.loc[t['frame'] == framenr]['y']) / len(t.loc[t['frame'] == framenr]['x']))
        except:
            try: 
                x.append(x[-1])
                y.append(y[-1])
            except:
                x.append(0)
                y.append(0)

    v_x = (np.insert(x, 0, 0) - np.insert(x, -1, 0))[1:-1] / (np.insert(framelist, 0, 0) - np.insert(framelist, -1, 0))[1:-1]
    v_y = (np.insert(y, 0, 0) - np.insert(y, -1, 0))[1:-1] / (np.insert(framelist, 0, 0) - np.insert(framelist, -1, 0))[1:-1]
    velocity = np.sqrt(np.square(x) + np.square(y))

    displacement = []
    averageSpeed = []
    for i in list(set(t['particle'])):
        tt = t.loc[t['particle'] == i]
        tt = tt.reset_index()
        S = 0 
        for j in range(1, len(tt['x'])):
            ds = np.sqrt((tt['x'].iloc[j] - tt['x'].iloc[j - 1])**2 + (tt['y'].iloc[j] - tt['y'].iloc[j - 1])**2)
            S = S + ds
        displacement.append(S)
        averageSpeed.append(S/duration)

    plt.title(f'{filename}')
    plt.plot(framelist, velocity)
    plt.xlabel('frame nr')
    plt.ylabel('velocity (pixels/frame)')
    plt.xlim(min(framelist), max(framelist))
    plt.savefig(f'{graphs_path}\\velocity_{filename}.png', dpi=500, bbox_inches='tight')
    plt.clf()

    velocitydata.append((filename, pd.DataFrame({
                                                'particle':  list(set(t['particle'])),
                                                'displacement' : displacement,
                                                'averageSpeed' : averageSpeed})))
    
    plt.axes().set_aspect('equal')
    if t['particle'].max() != 0:
        for i in list(set(t['particle'])):
            tt = t.loc[t['particle']==i]
            plt.plot(tt['x'], tt['y'], label = i)
    else:
        tt = t.loc[t['particle']==0]
        plt.scatter(tt['x'], tt['y'], c = tt['frame'], s = 0.7)
        plt.plot(tt['x'], tt['y'], color = 'black', zorder = -10, linewidth = 0.5)

    plt.title(f'{filename}')
    plt.imshow(frames[0], zorder = -20)
    plt.savefig(f'{graphs_path}\\trajectories_{filename}.png', dpi=500, bbox_inches='tight')
    plt.clf()
    plt.close('all')

    filedata.append((filename, list(framelist), list(theta), list(omega), list(velocity)))

print('FINISHED ALL TRACKING ANALYSES')

print('\n velocity results:')
for data in velocitydata:
    print(data[0], '\n', data[1], '\n')

# save the data to a txt file as I am lazy (you can read it in with the open() and eval() functions)
with open("trackingdata.txt", 'w') as output:
    for row in filedata:
        output.write(str(row) + '\n')

max_frame = 0
