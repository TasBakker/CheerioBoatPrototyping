# Guide for Active Cheerio 3D-printing
![printprocess](https://github.com/user-attachments/assets/07f0eeb4-acfe-40e5-a2db-4edd8781d27b)

This guide provides detailed steps to fabricate Alcohol-powered Cheerios-inspired devices that are 3D printable and designed to operate on the surface of water.

The information provided is from the current preprint: [Wilt, J. K., Schramma, N., Bottermans, J. W., & Jalaal, M. (2024). "ActiveCheerios: 3D-Printed Marangoni-Driven Active Particles at an Interface." arXiv preprint arXiv:2411.16011.](https://arxiv.org/pdf/2411.16011)

## Materials and Equipment ##

**3D Printer:** Ultimaker S3 fused filament fabrication (FFF) machine. 

**Printing Material:** Polylactic acid (PLA) thermoplastic. In this study, red PLA was used, but any color is suitable. PLA is moderately biodegradable (under certain conditions). Alternative materials can be used while considering their density; biodegradable options are preferred for environmental sustainability.

## File Formats and Designs ##

Designs were created in a Computer-Aided Design (CAD) program. Examples of open source programs are [FreeCAD](https://www.freecad.org/) or potentially with an educational license [Fusion360](https://www.autodesk.com/campaigns/education/fusion-360-education?mktvar002=4246565|SEM|11094403127|142663428892|kwd-377987916670&ef_id=CjwKCAiA6t-6BhA3EiwAltRFGPIyp9j75XEVfvkBnsBDCAecH_xo9sXrgq0ZP6SiswMxOjQ8qb3auRoC53MQAvD_BwE:G:s&s_kwcid=AL!11172!3!602367525071!p!!g!!fusion360%20education!11094403127!142663428892&mkwid=s|pcrid|602367525071|pkw|fusion360%20education|pmt|p|pdv|c|slid||pgrid|142663428892|ptaid|kwd-377987916670|pid|&utm_medium=cpc&utm_source=google&utm_campaign=&utm_term=fusion360%20education&utm_content=s|pcrid|602367525071|pkw|fusion360%20education|pmt|p|pdv|c|slid||pgrid|142663428892|ptaid|kwd-377987916670|&gad_source=1&gclid=CjwKCAiA6t-6BhA3EiwAltRFGPIyp9j75XEVfvkBnsBDCAecH_xo9sXrgq0ZP6SiswMxOjQ8qb3auRoC53MQAvD_BwE). File types included are stereolithography (STL) files which are 3D files ready to be 3D printed and STEP files which you can import to your CAD program to modify!

**Files in this repository:**

**SingleOutlet_cheerio** - Single-hole outlet design as the primary cheerio in the study for ballistic-like movement.

**DualOutlet_cheerio** - Two-outlet design particle used less in the study for complex instability. 

**Chiral_cheerio** - Chiral device used as a spinning cheerio in the study.

**trackingcap** - Tracking caps used for computer vision and tracking of the Cheerios, which were colored with paint markers.

**Extra_Designs**—The extra folder contains exploratory designs for customization, including "hare-brained" ideas, heavily modified Cheerios and additional adornments to create interesting interparticle interactions.

## Printing Settings ##

Load the STL or STEP file into your slicing software. Choose the desired layer refinement level (preferably ultra-fine). Begin the printing process. Post-processing: Inspect the printed device. Use a fine needle to clear any blockages in the hole(s) caused by layer inaccuracies.

**Infill:** Approximately 10%. Ensures sufficient buoyancy and structural rigidity. Reduces errors during printing, especially for long spans. 

**Layer height:** Ultra-fine settings for high precision. Any refinement level is viable but may require post-processing because the hole may become blocked, which can be manually fixed by clearing the outlet with a needle. 

**Typical Print Time:** 15–20 minutes per device, depending on settings.


## Notes for Users ##

Exploration and Customization: The additional designs not included in the study are provided for further experimentation. STEP files allow users to modify dimensions and adapt designs in CAD software. If using non-PLA materials, consider their environmental impact and compatibility with water-based operation and disposal procedure after use. By following these instructions, you can successfully fabricate and experiment with Cheerios-inspired devices for use on water surfaces. Adjust and innovate based on your specific needs and applications!

