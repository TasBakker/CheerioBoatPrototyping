# Fork for course Prototyping
This is a fork of an existing project for use in the course prototyping. The original repository is located at: https://github.com/FluidLab/Active_Cheerio_3Dprinting. 

# Guide for Active Cheerio 3D-printing
![printprocess](https://github.com/user-attachments/assets/07f0eeb4-acfe-40e5-a2db-4edd8781d27b)

This guide provides detailed steps to fabricate Alcohol-powered Cheerios-inspired devices that are 3D printable and designed to operate on the surface of water.

The information provided is from the current preprint: [Wilt, J. K., Schramma, N., Bottermans, J. W., & Jalaal, M. (2024). "ActiveCheerios: 3D-Printed Marangoni-Driven Active Particles at an Interface." arXiv preprint arXiv:2411.16011.](https://arxiv.org/pdf/2411.16011)

## Materials and Equipment ##

**3D Printer:** Bambulabs X1-c and Prusa MK4/XL fused filament fabrication (FFF) machines. 

**Printing Material:** Generic PLA and TPU.

## File Formats and Designs ##

Designs were created in a Computer-Aided Design (CAD) program. Examples of open source programs are [FreeCAD](https://www.freecad.org/) or potentially with an educational license [Fusion360](https://www.autodesk.com/campaigns/education/fusion-360-education?mktvar002=4246565|SEM|11094403127|142663428892|kwd-377987916670&ef_id=CjwKCAiA6t-6BhA3EiwAltRFGPIyp9j75XEVfvkBnsBDCAecH_xo9sXrgq0ZP6SiswMxOjQ8qb3auRoC53MQAvD_BwE:G:s&s_kwcid=AL!11172!3!602367525071!p!!g!!fusion360%20education!11094403127!142663428892&mkwid=s|pcrid|602367525071|pkw|fusion360%20education|pmt|p|pdv|c|slid||pgrid|142663428892|ptaid|kwd-377987916670|pid|&utm_medium=cpc&utm_source=google&utm_campaign=&utm_term=fusion360%20education&utm_content=s|pcrid|602367525071|pkw|fusion360%20education|pmt|p|pdv|c|slid||pgrid|142663428892|ptaid|kwd-377987916670|&gad_source=1&gclid=CjwKCAiA6t-6BhA3EiwAltRFGPIyp9j75XEVfvkBnsBDCAecH_xo9sXrgq0ZP6SiswMxOjQ8qb3auRoC53MQAvD_BwE). File types included are 3D manufacturing format (3mf) and fusion 360 archive files (f3d). 

**Files in this repository:**

**trackingcode.ipynb** - A jupyter notebook file for processing video recordings of cheerio boats with tracking caps attached. Note: each lobe of the tracking cap should be either bright red, green or blue!

**blucktracking.py** - An adaptation of the notebook for processing bulk amounts of video.

**cheeriomass.ipynb** - A jupyter notebook file for estimating the height of the cheerio boat flotation 

**cheerio_single_nozzle** - Single-hole outlet on a rotatable nozzle including fins based off of the models from the original repository.

**cheerio_modular** - A modular cheerio boat design intended to be used with plugs. 

**cheerio_outlet_module** - A module for the modular cheerio with a single outlet.

**cheerio_triple_channel** - A derivation of the single nozzle design, with two added fixed channels at an angle of 40 degrees from the rotatable nozzle.

**multitrackingcap** — Different designs for a tracking cap te be used for linking or tracking cheerios.

## Printing Settings ##

Load the STL or STEP file into your slicing software. Choose the desired layer refinement level (preferably ultra-fine). Begin the printing process. Post-processing: Inspect the printed device. Use a fine needle to clear any blockages in the hole(s) caused by layer inaccuracies.
The nozzle can be printed with TPU to decrease leakage but is prone to printing failure.

**Infill:** Approximately 10%. Ensures sufficient buoyancy and structural rigidity. Reduces errors during printing, especially for long spans. 

**Layer height:** Ultra-fine settings for high precision. Any refinement level is viable but may require post-processing because the hole may become blocked, which can be manually fixed by clearing the outlet with a needle. 

**Typical Print Time:** 20-25 minutes per device, depending on settings.
