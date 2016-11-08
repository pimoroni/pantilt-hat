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

    def read_byte_data(self, addr, reg, data):
        global regs

        return regs[reg]

        self._debug(addr, reg, data)


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

import pantilthat

# Config Register
# Bit  8 - N/A
# Bit 7 - N/A
# Bit 6 - N/A
# Bit 5 - Light On
# Bit 4 - Light Mode: 0 = PWM, 1 = WS2812
# Bit 3 - Enable Lights
# Bit 2 - Enable Servo 2
# Bit 1 - Enable Servo 1

print("Testing constants...")
assert pantilthat.WS2812 == 1, "pantilthat.WS2812 should equal 1"
assert pantilthat.PWM == 0, "pantilthat.PWM should equal 0"
print("OK!")

# print("\nInstantiating library...")
# pt = pantilthat.PanTilt()
pt = pantilthat

assert regs[REG_CONFIG] == 0b00001111, "Config reg incorrect!: {}".format(regs[REG_CONFIG])
print("OK!")

print("Testing servo aliases...")
assert pt.pan == pt.servo_one, "Method 'pan' should alias 'servo_one'"
assert pt.tilt == pt.servo_two, "Method 'tilt' should alias 'servo_two'"
print("OK!")

print("\nSetting known good config...")
pt.servo_enable(1,True)
pt.servo_enable(2,True)

pt.servo_pulse_min(1,510)
pt.servo_pulse_max(1,2300)

pt.servo_pulse_min(2,510)
pt.servo_pulse_max(2,2300)

print("\n=== SERVOS ===")

print("\nSetting servo one to 0 degrees...")
i2c_assert(lambda:pt.servo_one(0), 
           lambda:regs[REG_SERVO1] == 5 and regs[REG_SERVO1 + 1] == 125,
           "Servo 1 regs contain incorrect value!")
print("OK!")

print("\nSetting servo two to 0 degrees...")
i2c_assert(lambda:pt.servo_two(0),
           lambda:regs[REG_SERVO2] == 5 and regs[REG_SERVO2 + 1] == 125,
           "Servo 2 regs contain incorrect value!")
print("OK!")

print("\nTesting full sweep...")
# Perform a full sweep to catch any bounds errors
for x in range(-90,91):
	pt.pan(x)
	pt.tilt(x)
for x in reversed(range(-90,91)):
	pt.pan(x)
	pt.tilt(x)
print("OK!")

print("\nTesting servo_enable...")
pt.servo_enable(1,False)
pt.servo_enable(2,False)

assert regs[REG_CONFIG] == 0b00001100, "Config reg {} incorrect! Should be 0b00001100".format(regs[REG_CONFIG])
print("OK")

print("\n=== LIGHTS ===")

print("\nTesting range checks...")
assert_raises(lambda:pt.set_pixel(34, 255, 255, 255), ValueError, "ValueError not raised by set_pixel index out of range")
print("OK! - ValueError raised by set_pixel index of out range.")
assert_raises(lambda:pt.set_pixel(0, 256, 0, 0), ValueError, "ValueError not raised by set_pixel colour out of range")
print("OK! - ValueError raised by colour out of range.")

print("\nTesting set_pixel...")
pt.set_pixel(0, 255, 255, 255)

i2c_assert(lambda:pt.show(),
           lambda:sum(regs[REG_WS2812:REG_WS2812 + 72]) == 255 * 3 and regs[REG_UPDATE] == 1,
           "WS2812 regs contain incorrect value!")
print("OK!")

print("\nTesting set_all...")
pt.set_all(255, 255, 255)

i2c_assert(lambda:pt.show(),
           lambda:sum(regs[REG_WS2812:REG_WS2812 + 72]) == 255 * 3 * 24 and regs[REG_UPDATE] == 1,
           "WS2812 regs contain incorrect value!")
print("OK!")

print("\nChanging light mode...")
pt.light_mode(pantilthat.PWM)
assert regs[REG_CONFIG] == 0b00000100 # The servos were disabled above
print("OK!")

print("\nWell done, you've not broken anything!") # I'll never forgive myself :D

