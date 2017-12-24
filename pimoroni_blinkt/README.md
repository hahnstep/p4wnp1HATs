Basic HAT Support
=================

Author : hahnstep (https://github.com/hahnstep)

Credits :

P4wnP1 is made by Mame82 : https://github.com/mame82

## Supported HATs

PIMORONI_BLINKT https://shop.pimoroni.com/products/blinkt

## Setup

     cd /home/pi/P4wnP1
     git clone https://github.com/hahnstep/p4wnp1HATs
     cd pimoroni_blinkt
     sudo ./install 

install system service for led_blink sopport 

     cd /home/pi/P4wnP1/p4wnp1HATs
     sudo ./install 

add to setup.cfg before payload section 

     # ========================
     # Settings for HAT support
     # ========================

     PIMORONI_BLINKT=true   # Pimoroni Blinkt ( 8 rgb Leds )

led_blink with PIMORONI_BLINKT enabled

     led_blink 1 turn on 1 led
     led_blink 2 turn on 2 leds
     led_blink 3 turn on 3 leds

     and so on

     led_blink 0 turn all leds off
 
