#!/bin/sh

wdir=/home/pi/P4wnP1

. $wdir/setup.cfg

 if $PIMORONI_BLINKT ; then
   $wdir/p4wnp1HATs/pimoroni_blinkt/ledtool.py & 
 fi
