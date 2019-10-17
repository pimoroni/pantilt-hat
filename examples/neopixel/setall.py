#!/usr/bin/env python

import sys
from sys import argv
import pantilthat

if len(argv)<2 or len(argv)>5:
    sys.stderr.write( "Syntax: {0} [<red> <green> <blue>] [<white>]\n".format(argv[0]) )
    exit(1)

red   = int(argv[1]) if len(argv)>3 else 0
green = int(argv[2]) if len(argv)>3 else 0
blue  = int(argv[3]) if len(argv)>3 else 0
white = int(argv[4]) if len(argv)>4 else 0
white = int(argv[1]) if len(argv)==2 else white

pantilthat.light_mode(pantilthat.WS2812)
pantilthat.light_type(pantilthat.GRBW)
pantilthat.set_all(red, green, blue, white)
pantilthat.show()
