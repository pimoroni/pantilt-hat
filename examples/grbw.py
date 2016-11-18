import pantilthat
import time
import math
import colorsys

pantilthat.light_mode(pantilthat.WS2812)

while True:
    for x in range(18):
        pantilthat.set_pixel_rgbw(x, 0, 0, 0, 255)

    pantilthat.show()

    p = int(math.sin(time.time()) * 90)
    t = int(math.sin(time.time()) * 90)

    pantilthat.pan(p)
    pantilthat.tilt(t)
