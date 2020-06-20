#!/bin/bash

# xinput --list-props SynPS/2 Synaptics TouchPad / 18

synclient FingerHigh=50
synclient FingerLow=45

xinput --set-prop 13 "Synaptics Noise Cancellation" 30 30
# xinput --set-prop 13 "Synaptics Finger" 43 47 255

synclient HorizTwoFingerScroll=1

synclient VertScrollDelta=-600
synclient HorizScrollDelta=-600

# synclient MaxSpeed=1.0
# synclient MinSpeed=0.7

synclient MaxSpeed=0.6
synclient MinSpeed=0.1

synclient AccelFactor=0.01

synclient MaxTapTime=100

synclient PalmDetect=1
synclient PalmMinWidth=10
synclient PalmMinZ=0

