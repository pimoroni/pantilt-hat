"""Library for Pimoroni Blinkt! programs compatibility with a Pimoroni Pan-Tilt HAT and an Adafruit Neopixel strip"""
import sys
import pantilthat
import atexit
import signal

_clear_on_exit = True
_brightness    = 0.2
NUM_PIXELS     = 8
pixels = [[0, 0, 0, _brightness]] * NUM_PIXELS

def _exit():
    if _clear_on_exit:
        clear()
        show()


def set_brightness(brightness):
    """Set the brightness of all pixels

    :param brightness: Brightness: 0.0 to 1.0
    """

    if brightness < 0 or brightness > 1:
        raise ValueError("Brightness should be between 0.0 and 1.0")

    global _brightness
    _brightness = brightness


def clear():
    pixels[:] = [[0, 0, 0, _brightness]] * NUM_PIXELS
    pantilthat.clear()


def show():
    pantilthat.show()


def set_all(r, g, b, brightness=None):
    global _brightness
    if brightness is not None:
        _brightness = brightness
    pixels[:] = [[r, g, b, _brightness]] * NUM_PIXELS
    pantilthat.set_all(int(r*_brightness), int(g*_brightness), int(b*_brightness))

def get_pixel(x):
    return pixels[0]

def set_pixel(x, r, g, b, brightness=None):
    global _brightness
    if brightness is not None:
        _brightness = brightness
    pixels[x] = [r, g, b, _brightness]
    pantilthat.set_pixel(x, int(r*_brightness), int(g*_brightness), int(b*_brightness))


def set_clear_on_exit(value=True):
    """Set whether Blinkt! should be cleared upon exit

    By default Blinkt! will turn off the pixels on exit, but calling::

        blinkt.set_clear_on_exit(False)

    Will ensure that it does not.

    :param value: True or False (default True)
    """
    global _clear_on_exit
    _clear_on_exit = value


def interrupt_handler(signum, frame):
    print("\rKeyboardInterrupt")
    sys.exit(128+signum)


# Module Initialisation
pantilthat.light_mode(pantilthat.WS2812)
pantilthat.light_type(pantilthat.GRBW)
atexit.register(_exit)
signal.signal(signal.SIGINT, interrupt_handler)
