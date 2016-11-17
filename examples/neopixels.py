import pantilthat as pt
import time
import math
import colorsys

pt.light_mode(pt.WS2812)

while True:
    t = time.time()
    b = (math.sin(t * 2) + 1) / 2
    b = int(b * 255.0)
    t = round(time.time() * 1000) / 1000
    a = round(math.sin(t) * 90)
    pt.pan(int(a))
    pt.tilt(int(a))
    r, g, b = [int(x*255) for x in  colorsys.hsv_to_rgb(((t*100) % 360) / 360.0, 1.0, 1.0)]
    pt.set_all(r, g, b)
    pt.show()
    print(a)
    time.sleep(0.04)
