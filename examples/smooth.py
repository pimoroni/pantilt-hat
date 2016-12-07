#!/usr/bin/env python

import math
import time

import pantilthat


while True:
    # Get the time in seconds
    t = time.time()

    # G enerate an angle using a sine wave (-1 to 1) multiplied by 90 (-90 to 90)
    a = math.sin(t * 2) * 90

    pantilthat.pan(a)
    pantilthat.tilt(a)

    # Two decimal places is quite enough!
    print(round(a,2))

    # Sleep for a bit so we're not hammering the HAT with updates
    time.sleep(0.005)
