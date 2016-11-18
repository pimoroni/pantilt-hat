from sys import exit, version_info

try:
    from smbus import SMBus
except ImportError:
    if version_info[0] < 3:
        exit("This library requires python-smbus\nInstall with: sudo apt-get install python-smbus")
    elif version_info[0] == 3:
        exit("This library requires python3-smbus\nInstall with: sudo apt-get install python3-smbus")

from .pantilt import PanTilt, WS2812, PWM

__version__ = '0.0.1'

pantilthat = PanTilt(i2c_bus=SMBus(1))

brightness = pantilthat.brightness

clear = pantilthat.clear

light_mode = pantilthat.light_mode

servo_one = pantilthat.servo_one

servo_pulse_max = pantilthat.servo_pulse_max

servo_pulse_min = pantilthat.servo_pulse_min

servo_two = pantilthat.servo_two

servo_enable = pantilthat.servo_enable

set_all = pantilthat.set_all

set_pixel = pantilthat.set_pixel

set_pixel_rgbw = pantilthat.set_pixel_rgbw

show = pantilthat.show

pan = pantilthat.servo_one

tilt = pantilthat.servo_two
