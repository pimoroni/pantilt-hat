from sys import exit, version_info

try:
    from smbus import SMBus
except ImportError:
    if version_info[0] < 3:
        exit("This library requires python-smbus\nInstall with: sudo apt-get install python-smbus")
    elif version_info[0] == 3:
        exit("This library requires python3-smbus\nInstall with: sudo apt-get install python3-smbus")

from .pantilt import PanTilt, WS2812, PWM

pantilt = PanTilt(i2c_bus=SMBus(1))

def brightness(brightness):
    pantilt.brightness(brightness)

def clear():
    pantilt.clear()

def light_mode(mode):
    pantilt.light_mode(mode)

def servo_one(angle):
    pantilt.servo_one(angle)

def servo_pulse_max(index, value):
    pantilt.servo_pulse_max(index, value)

def servo_pulse_min(index, value):
    pantilt.servo_pulse_min(index, value)

def servo_two(angle):
    pantilt.servo_two(angle)

def servo_enable(index, state):
    pantilt.servo_enable(index, state)

def set_all(red, blue, green):
    pantilt.set_all(red, blue, green)

def set_pixel(index, red, blue, green):
    pantilt.set_pixel(index, red, blue, green)

def set_pixel_rgbw(index, red, blue, green, white):
    pantilt.set_pixel_rgbw(index, red, blue, green, white)

def show():
    pantilt.show()

pan = servo_one
tilt = servo_two
