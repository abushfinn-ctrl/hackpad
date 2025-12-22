# **FusionPad**
FusionPad is a 2x4 key macropad with a rotary encoder it uses KMK firmware


Features:
Two part 3d printer case
EC11 Rotary encoder for volume (can be changed for zoom)
8 Keys



# **CAD Model:**
The case screws together using 4 M3 bolts and headset inserts. One on each corner


Schematic

Made in Fusion360. Nifty

PCB
Here's my PCB! It was made in KiCad. The silkscreen was imported from a Figma image.

Schematic Schematic

PCB Schematic

I used MX_V2 for the keyswitch footprints. I think in retrospect, I should've added a ground plane

Firmware Overview
This hackpad uses QMK firmware for everything.

the rotary encoder changes volume. press to mute
The 4 keys currently act as macros I dynamically change in VIA.
The OLED is a cat!! Bongocat!! :3
Bongo Cat

I might add more in the future! That's it for now

BOM:
Here should be everything you need to make this hackpad

4x Cherry MX Switches
4x DSA Keycaps
5x M3x5x4 Heatset inserts
3x M3x16mm SHCS Bolts
2X M3x12mm SHCS Bolts
5x 1N4148 DO-35 Diodes.
2x WS2812B LEDs
1x 0.91" 128x32 OLED Display
1x EC11 Rotary Encoder
1x XIAO RP2040
1x Case (3 printed parts, 2 laser cut parts)
