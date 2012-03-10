#!/usr/bin/env python

import time
import random
from subprocess import *

def sh(cmd) :
  return Popen(cmd, shell=True, stdout=PIPE).stdout.read()

while True :
  if sh('wmctrl -l | grep "Call with"') :
    if not sh('wmctrl -l | grep "Full-Screen"') :
      # bring call window forward
      sh('wmctrl -R "Call with"')
      
      # send full screen command
      sh('xdotool keydown f')
      sh('xdotool keyup f')
    else :
      m = sh('xdotool getmouselocation')
      loc = m.split(' ')
      x = int(loc[0][2:])
      y = int(loc[1][2:])
      
      # jitter the mouse by one pixel randomly
      x += (random.random() * 3) - 1
      y += (random.random() * 3) - 1
      
      sh('xdotool mousemove %d %d' % (x, y))

  time.sleep(5)
