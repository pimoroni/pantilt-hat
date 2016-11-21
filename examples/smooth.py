#!/usr/bin/env python

import math
import time

import pantilthat


pantilthat.light_mode(pantilthat.PWM)

while True:
    b = (math.sin(time.time() * 2) + 1) / 2
    b = int(b * 255.0)
    t = round(time.time() * 1000) / 1000
    a = round(math.sin(t) * 90)
    pantilthat.pan(int(a))
    pantilthat.tilt(int(a))
    pantilthat.brightness(b)
    print(a)
    time.sleep(0.04)
