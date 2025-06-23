---
title: "My Custom Keyboard"
author: "Haft"
description: "My very own custom keyboard, with its own PCB!"
created_at: "2025-06-20"
---

### **Total time working:** 18 hours, 11 minutes

> On hackatime the Fusion360 shows as <<LAST_PROJECT>>, the KiCAD shows as keyboard, and the KMK firmware shows as firmware

# June 20th, 2025

I have used this tutorial to make the PCB (of course, in an actual keyboard size and not just a 3x3 <br>
[![PCB Design Tutorial](https://img.youtube.com/vi/8WXpGTIbxlQ/maxresdefault.jpg)](https://youtu.be/8WXpGTIbxlQ)
### Schematic:
<img width="648" alt="image" src="https://github.com/user-attachments/assets/d21314b5-1044-498b-9ac7-4da744430cdd" /> <br>
### PCB Result:
<img width="580" alt="image" src="https://github.com/user-attachments/assets/685554ea-9305-4331-9b16-40134634a218" /> <br>
 <br>
A fully featured keyboard PCB for a 75% keyboard, with an oled screen and a knob. Tomorrow I expect a long day as I will be designing the 3D case for it. 
I have made multiple mistakes, like messing up the order of the switches, which took me 30 minutes to fix, accidentally connecting the screen to 3V3_EN instead of 3V3 and more.
**Total time today:** 3 hours, 11 minutes

# June 21st, 2025
I have updated unrouted lines that I missed in the PCB, and fixed a few more issues.
I also moved the OLED screen to the center, and replaced the main board from Pi Pico to ESP S3 Devkit C (took me 2 more hours).
The new schematic and PCB look like this:
<img width="551" alt="image" src="https://github.com/user-attachments/assets/5df69925-81c8-4dd0-90e6-dafefc0cdf03" />
<img width="609" alt="image" src="https://github.com/user-attachments/assets/62ae2502-7f26-464a-9911-03c9fc4f72f5" /> <br>
I also added 3 macro keys, and because I moved things around everything looks slimmer and better!
I had to reroute everything twice, and I recommend you guys to follow this rule: **Back for vertical, front for horizontal (or vise-varsa)**
I really recommend you check your PCB multiple times before making the case, it was really tedious to redo it after editing the PCB today (I first started with case, and only then made the PCB changes so I had to redo case)
Current case state:
<img width="564" alt="image" src="https://github.com/user-attachments/assets/c8dc96ba-8c8d-44b8-8238-0c6776a56f5d" /> <br>
I took about 2 hours for the case itself. And it's not done yet (need coloring, cutouts and a few more refinements)
**Total time today:** 5.5 hours 

# June 22nd, 2025
I changed the PCB once again, this time making it even slimmer and not bulky
<img width="530" alt="image" src="https://github.com/user-attachments/assets/3d5fbef5-3ea8-4d64-b3eb-8067ffd58abe" />
<img width="615" alt="image" src="https://github.com/user-attachments/assets/960422e9-17e4-4a94-873d-3500f9273ada" /> <br>

I'm very annoying at this point because I already changed the PCB three times and every time I have to redo the case, but, I mean, who am I to blame? The case looked bulky AF because of the PCB: <br> <img width="425" alt="image" src="https://github.com/user-attachments/assets/9d7c984f-a6b6-47a4-a657-f6b79a7acb94" /> <br>
This time, I'm going to make sure everything is slimmer so the keyboard doesnt look so bulky!
Finally done with that case! You should measure 3 times before making, I messed up my measurements multiple times, but now they're perfect!
Without switches & keycaps: <br> <img width="1121" alt="image" src="https://github.com/user-attachments/assets/42c73152-1142-4a15-a058-07a4b37d13f8" />
 <br>
With switches & keycaps: <br>  <img width="1144" alt="image" src="https://github.com/user-attachments/assets/6465d497-445c-4fe2-901d-dc8fe00f1c82" />
 <br>

 Now that the keyboard itself is done, all that's left is the software! Will do that tomorrow!!
 **Total time today:** 8.5 hours

 # June 23rd, 2025
There wasn't much to do today. Almost everything was done and all I did was the sofware. Iran woke me up 3 hours ago (10 am) because of their missiles, and I just finished the KMK firmware.
It was very simple and easy, I just followed the tutorial and in no time I was done!
There isn't any picture to show today, because it was just firmware. Check it out at firmware/main.py!

I also chose a new color pallete for the keyboard
<img width="955" alt="image" src="https://github.com/user-attachments/assets/fbf900f0-fd25-4499-85d5-57d582e85aff" />


**Total tiem today:** 1 hour
