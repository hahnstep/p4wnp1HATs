#!/bin/sh

wdir=$( cd $(dirname $BASH_SOURCE[0]) && cd .. && pwd)

. $wdir/setup.cfg

 if $PIMORONI_BLINKT ; then
   python $wdir/p4wnp1HATs/pimoroni_blinkt/ledtool.py "$1"
 fi
