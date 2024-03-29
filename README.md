# Pan-Tilt HAT
https://shop.pimoroni.com/products/pan-tilt-hat

Pan-Tilt HAT is a two-channel servo driver designed to control a tiny servo-powered Pan/Tilt assembly. It also controls either PWM-dimmed lights or WS2812 pixels; up to 24 RGB or 18 RGBW.

## Installing

### Full install (recommended):

We've created an easy installation script that will install all pre-requisites and get your Pan-Tilt HAT
up and running with minimal efforts. To run it, fire up Terminal which you'll find in Menu -> Accessories -> Terminal
on your Raspberry Pi desktop, as illustrated below:

![Finding the terminal](http://get.pimoroni.com/resources/github-repo-terminal.png)

In the new terminal window type the command exactly as it appears below (check for typos) and follow the on-screen instructions:

```bash
curl https://get.pimoroni.com/pantilthat | bash
```

### Manual install:

Enable i2c:

```bash
sudo raspi-config nonint do_i2c 0
```

Install the library:

```bash
python3 -m pip install pantilthat
```

ℹ️ Depending on your system, you might need to use `sudo` for the above command.

### Development:

If you want to contribute, or like living on the edge of your seat by having the latest code, you should clone this repository, `cd` to the library directory, and run:

```bash
sudo python3 setup.py install
```
(or `sudo python setup.py install` whichever your primary Python environment may be)

In all cases you will have to enable the i2c bus.

## Breakout Header Pinout

The breakout header on Pan Tilt HAT is connected directly to the GPIO pins.

Below is a map of the breakout functions and corresponding BCM pins:

| SDA | SCL | TX | RX | PWM | MOSI | MISO | SCLK | CEO |
| --- | --- | -- | -- | --- | ---- | ---- | ---- | --- |
| 2   | 3   | 14 | 15 | 18  | 10   | 9    | 11   | 8   |

## Documentation & Support

* Guides and tutorials - https://learn.pimoroni.com/pan-tilt-hat
* Function reference - http://docs.pimoroni.com/pantilthat/
* GPIO Pinout - https://pinout.xyz/pinout/pan_tilt_hat
* Get help - http://forums.pimoroni.com/c/support
