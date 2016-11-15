import pantilthat as pt
import time
import math

pt.light_mode(pt.PWM)

while True:
    b = (math.sin(time.time() * 2) + 1) / 2
    b = int(b * 255.0)
    t = round(time.time() * 1000) / 1000
    a = round(math.sin(t) * 90)
    pt.pan(int(a))
    pt.tilt(int(a))
    pt.brightness(b)
    print(a)
    time.sleep(0.04)
