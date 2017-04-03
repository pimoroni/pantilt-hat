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

Alternatively, on Raspbian, you can download the `pimoroni-dashboard` and install your product by browsing to the relevant entry:

```bash
sudo apt-get install pimoroni
```
(you will find the Dashboard under 'Accessories' too, in the Pi menu - or just run `pimoroni-dashboard` at the command line)

If you choose to download examples you'll find them in `/home/pi/Pimoroni/pantilthat/`.

### Manual install:

#### Library install for Python 3:

on Raspbian:

```bash
sudo apt-get install python3-pantilthat
```

other environments: 

```bash
sudo pip3 install pantilthat
```

#### Library install for Python 2:

on Raspbian:

```bash
sudo apt-get install python-pantilthat
```

other environments: 

```bash
sudo pip2 install pantilthat
```

### Development:

If you want to contribute, or like living on the edge of your seat by having the latest code, you should clone this repository, `cd` to the library directory, and run:

```bash
sudo python3 setup.py install
```
(or `sudo python setup.py install` whichever your primary Python environment may be)

In all cases you will have to enable the i2c bus.

## Documentation & Support

* Guides and tutorials - https://learn.pimoroni.com/pantilt-hat
* Function reference - http://docs.pimoroni.com/pantilthat/
* GPIO Pinout - https://pinout.xyz/pinout/pantilt_hat
* Get help - http://forums.pimoroni.com/c/support
