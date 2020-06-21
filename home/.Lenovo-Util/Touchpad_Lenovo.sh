#!/bin/bash


##################################################
# config for newer driver (xorg-xinput) [ manjaro ]
##################################################

berrabe="SynPS/2 Synaptics TouchPad"

# xinput --list-props "SynPS/2 Synaptics TouchPad" / 18

xinput --set-prop "$berrabe" "libinput Tapping Enabled" 1
xinput --set-prop "$berrabe" "libinput Natural Scrolling Enabled" 1
xinput --set-prop "$berrabe" "libinput Accel Speed" -0.500000



# xinput --set-prop 13 "Synaptics Noise Cancellation" 30 30
# xinput --set-prop 13 "Synaptics Finger" 43 47 255





##################################################
# config for legacy driver (xf86-input-synaptics) [ ubuntu ]
##################################################

# synclient MaxSpeed=1.0
# synclient MinSpeed=0.7

# synclient FingerHigh=50
# synclient FingerLow=45

# synclient MaxSpeed=0.6
# synclient MinSpeed=0.1

# synclient AccelFactor=0.01

# synclient MaxTapTime=100

# synclient PalmDetect=1
# synclient PalmMinWidth=10
# synclient PalmMinZ=0

# synclient HorizTwoFingerScroll=1

# synclient VertScrollDelta=-600
# synclient HorizScrollDelta=-600

