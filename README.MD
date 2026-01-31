
# **FusionPad**
FusionPad is a 2x4 key macropad with a rotary encoder it uses KMK firmware. I decided to make this because I recently switch from a logitech G502 with lots of buttons to a Bambu custom 3d printed mouse with no extra buttons. I then was able to have my fusions commands on my mouse so I decided to make a macropad specifically for Fusion. 




Features:
Two part 3d printer case
EC11 Rotary encoder for volume (can be changed for zoom)
8 Keys

# **How to build:**
Once your PCB arrives you can start soldering all the componenet into the correct spots, then you plug the Hackpad in and add the firmware. Easy Peasy.

# **CAD Model:**
The case screws together using 4 M3 bolts and headset inserts. One on each corner



<img width="1027" height="767" alt="Screenshot 2025-12-22 194414" src="https://github.com/user-attachments/assets/fbd49830-c499-45df-9233-187b1b07be77" />


# **PCB**
Here's my PCB! It was made in KiCad.\
<img width="577" height="594" alt="Screenshot 2025-12-22 194543" src="https://github.com/user-attachments/assets/1087b6b5-3ec7-4861-a9c3-61a3bb5cc309" />


# **PCB Schematic** 
Messy I know\
<img width="1172" height="597" alt="Screenshot 2025-12-22 194750" src="https://github.com/user-attachments/assets/0d18bbef-8e4c-41c7-8330-b9255ceb2619" />

I used MX_V2 for the keyswitch footprints.

# **Firmware Overview**
My hackpad uses KMK firmware for everything.

The rotary encoder changes volume. Click to mute
Can be changed to zoom in and out
The 8 keys currently act as common key shortcuts I use in fusion.

# **BOM:**
Here should be everything you need to make this hackpad

8x Cherry MX Switches\
8x DSA Keycaps\
4x M3x5x4 Heatset inserts\
4x M3x16mm SHCS Bolts\
1x EC11 Rotary Encoder\
1x XIAO RP2040\
1x Case (3d printed)
