.. role:: python(code)
   :language: python

Welcome
-------

This documentation will guide you through the methods available in the Pan Tilt HAT python library.

Pan-Tilt HAT lets you mount and control one of our pan-tilt modules right on top of your Raspberry Pi. The HAT and its on-board microcontroller let you independently drive the two servos (pan and tilt), as well as driving up to 24 regular LED (with PWM control) or NeoPixel RGB (or RGBW) LEDs

* More information - https://shop.pimoroni.com/products/pan-tilt-hat
* Get the code - https://github.com/pimoroni/pantilt-hat
* Get help - http://forums.pimoroni.com/c/support

At A Glance
-----------

.. autoclassoutline:: pantilthat.PanTilt
   :members:

Set Brightness
--------------

.. automethod:: pantilthat.pantilthat.brightness

Clear
-----

.. automethod:: pantilthat.pantilthat.clear

Set Light Mode
--------------

.. automethod:: pantilthat.pantilthat.light_mode

Pan
---

.. automethod:: pantilthat.pantilthat.pan

.. automethod:: pantilthat.pantilthat.servo_one

Tilt
----

.. automethod:: pantilthat.pantilthat.tilt

.. automethod:: pantilthat.pantilthat.servo_two

Servo Enable
------------

.. automethod:: pantilthat.pantilthat.servo_enable

Servo Pulse Min
---------------

.. automethod:: pantilthat.pantilthat.servo_pulse_min

Servo Pulse Max
---------------

.. automethod:: pantilthat.pantilthat.servo_pulse_max

Set All LEDs
------------

.. automethod:: pantilthat.pantilthat.set_all

Set A LED
---------

.. automethod:: pantilthat.pantilthat.set_pixel

Set A LED (RGBW)
----------------

.. automethod:: pantilthat.pantilthat.set_pixel_rgbw

Show
----

.. automethod:: pantilthat.pantilthat.show

Constants
---------

* :python:`WS2812 = 1` - used with :python:`pantilthat.light_mode` to set WS2812 LEDs
* :python:`PWM = 0` - used with :python:`pantilthat.light_mode` to set PWM dimmed LEDs

