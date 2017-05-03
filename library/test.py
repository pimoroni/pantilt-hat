import sys
import time
import mock


REG_CONFIG = 0x00
REG_SERVO1 = 0x01
REG_SERVO2 = 0x03
REG_WS2812 = 0x05
REG_UPDATE = 0x4e

regs =[0 for x in range(79)]

class SMBus:
    def __init__(self, bus_id):
        global regs

        regs[0] = 0 # 0x00: REG_CONFIG
        regs[0] = 0 # 0x01: REG_SERVO1
        regs[0] = 0
        regs[0] = 0 # 0x03: REG_SERVO2
        regs[0] = 0
        regs[0] = 0 # 0x05: REG_WS2812
        regs[0] = 0
        regs[78] = 0 #0x4E: REG_UPDATE

        self._watch_regs = {
            REG_CONFIG: 'REG_CONFIG',
            REG_SERVO1: 'REG_SERVO1',
            REG_SERVO2: 'REG_SERVO2',
            REG_WS2812: 'REG_WS2812',
            REG_UPDATE: 'REG_UPDATE'
        }

        self._watch_len = {
            REG_CONFIG: 1,
            REG_SERVO1: 2,
            REG_SERVO2: 2,
            REG_WS2812: 72, # 24 LEDs
            REG_UPDATE: 1
        }

    def _debug(self, addr, reg, data):
        global regs

        if reg in self._watch_regs.keys():
            name = self._watch_regs[reg]
            length = self._watch_len[reg]
            result = regs[reg:reg+length]
            #print("Writing {data} to {name}: {result}".format(data=data, addr=addr, reg=reg, name=name, result=result))

    def write_i2c_block_data(self, addr, reg, data):
        global regs

        self._debug(addr, reg, data)

        for index, value in enumerate(data):
            regs[reg + index] = value

    def write_word_data(self, addr, reg, data):
        global regs

        regs[reg] = (data >> 8) & 0xff
        regs[reg + 1] = data & 0xff
        self._debug(addr, reg, data)

    def write_byte_data(self, addr, reg, data):
        global regs

        regs[reg] = data & 0xff

        self._debug(addr, reg, data)

    def read_byte_data(self, addr, reg):
        global regs

        return regs[reg]

    def read_word_data(self, addr, reg):
        global regs

        return (regs[reg] << 8) | regs[reg + 1]


def i2c_assert(action, expect, message):
    action()
    assert expect(), message

def assert_raises(action, expect, message):
    try:
        action()
    except expect:
        return

    print(message)
    sys.exit(1)


smbus = mock.Mock()
smbus.SMBus = SMBus

sys.modules['smbus'] = smbus
sys.path.insert(0, ".")

import pantilthat



#print("Testing help...")
#time.sleep(1)
#help(pantilthat.brightness)
#help(pantilthat.pan)

print("\nTesting constants...")
assert pantilthat.WS2812 == 1, "pantilthat.WS2812 should equal 1"
assert pantilthat.PWM == 0, "pantilthat.PWM should equal 0"
assert pantilthat.RGB == 0, "pantilthat.RGB should equal 0"
assert pantilthat.GRB == 1, "pantilthat.GRB should equal 1"
assert pantilthat.RGBW == 2, "pantilthat.RGBW should equal 2"
assert pantilthat.GRBW == 3, "pantilthat.GRBW should equal 3"
print("OK!")

pt = pantilthat

# Config Register
# Bit  8 - N/A
# Bit 7 - N/A
# Bit 6 - N/A
# Bit 5 - Light On
# Bit 4 - Light Mode: 0 = PWM, 1 = WS2812
# Bit 3 - Enable Lights
# Bit 2 - Enable Servo 2
# Bit 1 - Enable Servo 1
#
# Library should start up with servo1 and servo2 disabled
# and the light mode should default to WS2812, enabled
assert regs[REG_CONFIG] == 0b00001100, "Config reg incorrect!: {}".format(regs[REG_CONFIG])
print("OK!")

# Check every method we expect to exit, actually exists
print("\nTesting for API consistency...")
for method in ["idle_timeout", "servo_enable", "servo_pulse_max", "servo_pulse_min",
               "brightness", "clear", "light_mode", "light_type", "set_all",
               "set_pixel", "set_pixel_rgbw", "show",
               "servo_one", "pan", "get_pan", "get_servo_one",
               "servo_two", "tilt", "get_tilt", "get_servo_two"]:

    assert hasattr(pt, method), "Method {method}() should exist!".format(method=method)
    assert callable(getattr(pt, method)), "Method {method}() should be callable!".format(method=method)
print("OK!")

print("\nTesting servo aliases...")
assert pt.pan == pt.servo_one, "Method 'pan' should alias 'servo_one'"
assert pt.tilt == pt.servo_two, "Method 'tilt' should alias 'servo_two'"
assert pt.get_pan == pt.get_servo_one, "Method 'get_pan' should alias 'get_servo_one'"
assert pt.get_tilt == pt.get_servo_two, "Method 'get_tilt' should alias 'get_servo_two'"
print("OK!")

print("\nSetting known good config...")
pt.servo_enable(1, True)
pt.servo_enable(2, True)

pt.servo_pulse_min(1, 510)
pt.servo_pulse_max(1, 2300)

pt.servo_pulse_min(2, 510)
pt.servo_pulse_max(2, 2300)

print("\n=== SERVOS ===")

print("\nSetting servo one to 0 degrees...")
i2c_assert(lambda: pt.servo_one(0), 
           lambda: regs[REG_SERVO1] == 5 and regs[REG_SERVO1 + 1] == 125,
           "Servo 1 regs contain incorrect value!")
print("OK!")

print("\nSetting servo two to 0 degrees...")
i2c_assert(lambda: pt.servo_two(0),
           lambda: regs[REG_SERVO2] == 5 and regs[REG_SERVO2 + 1] == 125,
           "Servo 2 regs contain incorrect value!")
print("OK!")

print("\n=== READBACK ===")

for x in range(-90, 91):
    pt.pan(x)
    pt.tilt(x)
    #print("Pan  {}, got {}".format(x, pt.get_pan()))
    #print("Tilt {}, got {}".format(x, pt.get_tilt()))
    assert pt.get_pan() == x, "get_pan() should return {}, returned {}".format(x, pt.get_pan())
    assert pt.get_tilt() == x, "get_tilt() should return {}, returned {}".format(x, pt.get_tilt())

print("\nTesting full sweep...")
# Perform a full sweep to catch any bounds errors
for x in range(-90, 91):
    pt.pan(x)
    pt.tilt(x)
for x in reversed(range(-90, 91)):
    pt.pan(x)
    pt.tilt(x)
print("OK!")

print("\nTesting servo_enable...")
pt.servo_enable(1,False)
pt.servo_enable(2,False)

assert regs[REG_CONFIG] == 0b00001100, "Config reg {config:08b} incorrect! Should be 00001100".format(config=regs[REG_CONFIG])
print("OK")

print("\nTesting value/range checks...")

assert_raises(lambda: pt.servo_enable(3, True), ValueError,
              "ValueError not raised by servo_enable index out of range")
print("OK! - ValueError raised by servo_enable index of out range.")

assert_raises(lambda: pt.servo_enable(1, "banana"), ValueError,
              "ValueError not raised by servo_enable value invalid")
print("OK! - ValueError raised by servo_enable value invalid.")

assert_raises(lambda: pt.servo_pulse_min(3, 510), ValueError,
              "ValueError not raised by servo_pulse_min index out of range")
print("OK! - ValueError raised by servo_pulse_min index of out range.")

assert_raises(lambda: pt.servo_pulse_max(3, 510), ValueError,
              "ValueError not raised by servo_pulse_min index out of range")
print("OK! - ValueError raised by servo_pulse_min index of out range.")

print("\n=== LIGHTS ===")

print("\nTesting range checks...")

assert_raises(lambda: pt.set_pixel(34, 255, 255, 255), ValueError,
              "ValueError not raised by set_pixel index out of range")
print("OK! - ValueError raised by set_pixel index of out range.")

assert_raises(lambda: pt.set_pixel(0, 256, 0, 0), ValueError,
              "ValueError not raised by set_pixel colour out of range")
print("OK! - ValueError raised by colour out of range.")

print("\nTesting set_pixel...")
pt.set_pixel(0, 255, 255, 255)

i2c_assert(lambda: pt.show(),
           lambda: sum(regs[REG_WS2812:REG_WS2812 + 72]) == 255 * 3 and regs[REG_UPDATE] == 1,
           "WS2812 regs contain incorrect value!")
print("OK!")

print("\nTesting set_all...")
pt.set_all(255, 255, 255)

i2c_assert(lambda: pt.show(),
           lambda: sum(regs[REG_WS2812:REG_WS2812 + 72]) == 255 * 3 * 24 and regs[REG_UPDATE] == 1,
           "WS2812 regs contain incorrect value!")
print("OK!")

print("\nChecking brightness ignored in WS2812 mode...")
expected = 255
pt.brightness(222)
assert regs[REG_WS2812] == 255, "Brightness has affected WS2812 mode. REG_WS2812 is {} should be {}".format(regs[REG_WS2812], expected)
print("OK!")

print("\nChanging light mode...")
expected = 0b00000100
pt.light_mode(pantilthat.PWM)
assert regs[REG_CONFIG] == expected, "Failed to change light mode. REG_CONFIG is {0:08b} should be {1:08b}".format(regs[REG_CONFIG], expected) # The servos were disabled above
print("OK!")

print("\nChanging brightness...")
expected = 123
pt.brightness(expected)
assert regs[REG_WS2812] == expected, "Failed to change rightness. REG_WS2812 is {} should be {}".format(regs[REG_WS2812], expected)
print("OK!")

print("\nWell done, you've not broken anything!") # I'll never forgive myself :D