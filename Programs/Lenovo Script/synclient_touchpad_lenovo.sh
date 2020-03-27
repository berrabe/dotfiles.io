#!/bin/bash

# xinput --list-props SynPS/2 Synaptics TouchPad / 18

synclient FingerHigh=47
synclient FingerLow=43

synclient HorizTwoFingerScroll=1

synclient VertScrollDelta=-350
synclient HorizScrollDelta=-350

synclient MaxSpeed=1.0
synclient MinSpeed=0.7

synclient AccelFactor=0.01

synclient MaxTapTime=100

synclient PalmDetect=1
synclient PalmMinWidth=10
synclient PalmMinZ=0