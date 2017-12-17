#!/usr/bin/env python

import sys
import time
import blinkt

#blinkt.set_clear_on_exit(False)
blinkt.set_brightness(0.05)

def main(count):

  if count == 0:
    blinkt.set_all(0,0,0)
  else:
    for i in range(count):
       blinkt.set_pixel(i, 255, 255, 255)
       blinkt.show()
       time.sleep(0.05)

    time.sleep(0.3)


if __name__ == "__main__":
#        if len(sys.argv) < 1:
#        sys.exit()
        main(int(sys.argv[1]))
