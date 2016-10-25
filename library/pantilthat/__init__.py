from sys import exit, version_info

try:
    from smbus import SMBus
except ImportError:
    if version_info[0] < 3:
        exit("This library requires python-smbus\nInstall with: sudo apt-get install python-smbus")
    elif version_info[0] == 3:
        exit("This library requires python3-smbus\nInstall with: sudo apt-get install python3-smbus")

class LightMode:
    WS2812 = 1
    PWM = 0

class PanTilt:
    """PanTilt HAT Driver

    Communicates with PanTilt HAT over i2c 
    to control pan, tilt and light functions

    """
    REG_CONFIG = 0x00
    REG_SERVO1 = 0x01
    REG_SERVO2 = 0x03
    REG_WS2812 = 0x05
    REG_UPDATE = 0x4E
    UPDATE_WAIT = 0.03
    NUM_LEDS = 24

    def __init__(self,
        enable_servo1 = True,
        enable_servo2 = True,
        enable_lights = True,
        light_mode = LightMode.WS2812,
        servo1_min = 510,
        servo1_max = 2300,
        servo2_min = 510,
        servo2_max = 2300,
        address = 0x15):

        self._enable_servo1 = enable_servo1
        self._enable_servo2 = enable_servo2
        self._enable_lights = enable_lights
        self._light_on = 0

        self._servo_min = [servo1_min, servo2_min]
        self._servo_max = [servo1_max, servo2_max]

        self._light_mode = light_mode

        self.clear()

        self._i2c_address = address
        self._i2c = SMBus(1)
        self._set_config()

    def _set_config(self):
        """Generate config value for PanTilt HAT and write to device."""

        config = 0
        config |= self._enable_servo1
        config |= self._enable_servo2 << 1
        config |= self._enable_lights << 2
        config |= self._light_mode    << 3
        config |= self._light_on      << 4

        self._i2c_write_byte(self.REG_CONFIG, config)

    def _check_int_range(self, value, value_min, value_max):
        """Check the type and bounds check an expected int value."""

        if type(value) is not int:
            raise TypeError("Value should be an integer")
        if value < value_min or value > value_max:
            raise ValueError("Value {value} should be between {min} and {max}".format(
                value=value, 
                min=value_min, 
                max=value_max))

    def _servo_degrees_to_us(self, angle, us_min, us_max):
        """Converts degrees into a servo pulse time in microseconds

        :param angle: Angle in degrees from -90 to 90

        """

        self._check_int_range(angle, -90, 90)

        angle += 90
        servo_range = us_max - us_min
        us = (servo_range / 180.0) * angle
        return us_min + int(us)

    def _servo_range(self, servo_index):
        """Get the min and max range values for a servo"""

        return (self._servo_min[servo_index], self._servo_max[servo_index])

    def _i2c_write_block(self, reg, data):
        if type(data) is list:
            self._i2c.write_i2c_block_data(self._i2c_address, reg, data)
        else:
            raise ValueError("Value must be a list")

    def _i2c_write_word(self, reg, data):
        if type(data) is int:
            self._i2c.write_word_data(self._i2c_address, reg, data)

    def _i2c_write_byte(self, reg, data):
        if type(data) is int:
            self._i2c.write_byte_data(self._i2c_address, reg, data)

    def _i2c_read_byte(self, reg):
        return self._i2c.read_byte_data(self._i2c_address, reg)

    def clear(self):
        """Clear the buffer."""

        self._pixels = [0] * self.NUM_LEDS * 3
        self._pixels += [1]

    def light_mode(self, mode):
        """Set the light mode for attached lights.

        PanTiltHAT can drive either WS2812 pixels, 
        or provide a PWM dimming signal for regular LEDs.

        """

        self._light_mode = mode
        self._set_config()

    def brightness(self, brightness):
        """Set the brightness of the connected LED ring.

        :param brightness: Brightness from 0 to 255

        """

        self._check_int_range(brightness, 0, 255)

        # The brightness value is taken from the first register of the WS2812 chain
        self._i2c_write_byte(self.REG_WS2812, brightness)

    def set_all(self, red, green, blue):
        """Set all pixels in the buffer.

        :param red: Amount of red, from 0 to 255
        :param green: Amount of green, from 0 to 255
        :param blue: Amount of blue, from 0 to 255

        """

        for index in range(24):
            self.set_pixel(index, red, green, blue)

    def set_pixel(self, index, red, green, blue):
        """Set a single pixel in the buffer.

        :param index: Index of pixel from 0 to 23
        :param red: Amount of red, from 0 to 255
        :param green: Amount of green, from 0 to 255
        :param blue: Amount of blue, from 0 to 255

        """

        self._check_int_range(index, 0, 23)

        for c in [red, green, blue]:
            self._check_int_range(c, 0, 255)

        index *= 3
        self._pixels[index]   = red
        self._pixels[index+1] = green
        self._pixels[index+2] = blue

    def show(self):
        """Display the buffer on the connected WS2812 strip."""

        self._i2c_write_block(self.REG_WS2812,      self._pixels[:32])
        self._i2c_write_block(self.REG_WS2812 + 32, self._pixels[32:64])
        self._i2c_write_block(self.REG_WS2812 + 64, self._pixels[64:])
        self._i2c_write_byte(self.REG_UPDATE, 1)

    def servos_on(self, state):
        """Turn the servos on or off.

        :param state: Servo power: True = on, False = off

        """

        if state in [True,False]:
            self._servo_power = state
            self._set_config()
            return

        raise ValueError("State must be True/False")

    def servo_pulse_min(self, index, value):
        """Set the minimum high pulse for a servo in microseconds.

        :param value: Value in microseconds

        """

        if index not in [1,2]:
            raise ValueError("Servo index must be 1 or 2")
        
        self._servo_min[index-1] = value

    def servo_pulse_max(self, index, value):
        """Set the maximum high pulse for a servo in microseconds.

        :param value: Value in microseconds

        """

        if index not in [1,2]:
            raise ValueError("Servo index must be 1 or 2")
        
        self._servo_max[index-1] = value

    def servo_one(self, angle):
        """Set position of servo 1 in degrees.

        :param angle: Angle in degrees from -90 to 90

        """

        us_min, us_max = self._servo_range(0)
        us = self._servo_degrees_to_us(angle, us_min, us_max)
        self._i2c_write_word(self.REG_SERVO1, us)

    def servo_two(self, angle):
        """Set position of servo 2 in degrees.

        :param angle: Angle in degrees from -90 to 90

        """

        us_min, us_max = self._servo_range(1)
        us = self._servo_degrees_to_us(angle, us_min, us_max)
        self._i2c_write_word(self.REG_SERVO2, us)

    pan = servo_one
    tilt = servo_two

