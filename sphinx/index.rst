.. role:: python(code)
   :language: python

.. currentmodule:: pantilthat

Welcome
-------

This documentation will guide you through the methods available in the Pan Tilt HAT python library.

Pan-Tilt HAT lets you mount and control one of our pan-tilt modules right on top of your Raspberry Pi. The HAT and its on-board microcontroller let you independently drive the two servos (pan and tilt), as well as driving up to 24 regular LED (with PWM control) or NeoPixel RGB (or RGBW) LEDs

* More information - https://shop.pimoroni.com/products/pan-tilt-hat
* Get the code - https://github.com/pimoroni/pantilt-hat
* Get help - http://forums.pimoroni.com/c/support

At A Glance
-----------

.. autoclassoutline:: PanTilt
   :members:

Set Brightness
--------------

.. automethod:: pantilthat.brightness

Clear
-----

.. automethod:: pantilthat.clear

Set Light Mode & Type
---------------------

.. automethod:: pantilthat.light_mode

.. automethod:: pantilthat.light_type

Pan
---

.. automethod:: pantilthat.pan

.. automethod:: pantilthat.servo_one

.. automethod:: pantilthat.get_pan

Tilt
----

.. automethod:: pantilthat.tilt

.. automethod:: pantilthat.servo_two

.. automethod:: pantilthat.get_tilt

Servo Enable
------------

.. automethod:: pantilthat.servo_enable

Servo Idle Timeout
------------------

.. automethod:: pantilthat.idle_timeout

Servo Pulse Min
---------------

.. automethod:: pantilthat.servo_pulse_min

Servo Pulse Max
---------------

.. automethod:: pantilthat.servo_pulse_max

Set All LEDs
------------

.. automethod:: pantilthat.set_all

Set A LED
---------

.. automethod:: pantilthat.set_pixel

Set A LED (RGBW)
----------------

.. automethod:: pantilthat.set_pixel_rgbw

Show
----

.. automethod:: pantilthat.show

Constants
---------

* :python:`WS2812 = 1` - used with :python:`pantilthat.light_mode` to set WS2812/SK6812 LEDs
* :python:`PWM = 0` - used with :python:`pantilthat.light_mode` to set PWM dimmed LEDs

* :python:`RGB = 0` - used with :python:`pantilthat.light_type` to set RGB WS2812 LEDs
* :python:`GRB = 1` - used with :python:`pantilthat.light_type` to set GRB WS2812 LEDs
* :python:`RGBW = 2` - used with :python:`pantilthat.light_type` to set RGBW SK6812 LEDs
* :python:`GRBW = 3` - used with :python:`pantilthat.light_type` to set GRBW SK6812 LEDs
