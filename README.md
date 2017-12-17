Basic HAT Support
=================

Author : hahnstep (https://github.com/hahnstep)

Credits :

P4wnP1 is made by Mame82 : https://github.com/mame82

## Supported HATs

PIMORONI_BLINKT https://shop.pimoroni.com/products/blinkt

## Setup

'''
cd /home/pi/P4wnP1
git clone https://github.com/hahnstep/p4wnp1HATs
'''

run the install script 

add to setup.cfg before payload section 

''' 
# ========================
# Settings for HAT support
# ========================

PIMORONI_BLINKT=true   # Pimoroni Blinkt ( 8 rgb Leds )

''' 

