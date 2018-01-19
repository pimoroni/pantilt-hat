from sys import exit, version_info

try:
    from smbus import SMBus
except ImportError:
    if version_info[0] < 3:
        exit("This library requires python-smbus\nInstall with: sudo apt-get install python-smbus")
    elif version_info[0] == 3:
        exit("This library requires python3-smbus\nInstall with: sudo apt-get install python3-smbus")

from .pantilt import PanTilt, WS2812, PWM, RGB, GRB, RGBW, GRBW

__version__ = '0.0.4'

_is_setup = False
pantilthat = None

def setup():
    global _is_setup, pantilthat
    if _is_setup:
        return

    pantilthat = PanTilt(i2c_bus=SMBus(1))
    _is_setup = True

for method in "idle_timeout", "servo_enable", "servo_pulse_min", "servo_pulse_max", "brightness", "clear", "light_mode", "light_type", "set_all", "set_pixel", "set_pixel_rgbw", "show", "pan", "servo_one", "get_pan", "get_servo_one", "tilt", "servo_two", "get_tilt", "get_servo_two":
    def wrap(*args, **kwargs):
        setup()
        pantilthat.getattr(method)(*args, **kwargs)

    globals()[method] = wrap

#idle_timeout = pantilthat.idle_timeout
#servo_enable = pantilthat.servo_enable
#servo_pulse_max = pantilthat.servo_pulse_max
#servo_pulse_min = pantilthat.servo_pulse_min

#brightness = pantilthat.brightness
#clear = pantilthat.clear
#light_mode = pantilthat.light_mode
#light_type = pantilthat.light_type
#set_all = pantilthat.set_all
#set_pixel = pantilthat.set_pixel
#set_pixel_rgbw = pantilthat.set_pixel_rgbw
#show = pantilthat.show

#servo_one = pantilthat.servo_one
#pan = servo_one
#get_pan = get_servo_one = pantilthat.get_servo_one

#servo_two = pantilthat.servo_two
#tilt = servo_two
#get_tilt = get_servo_two = pantilthat.get_servo_two
