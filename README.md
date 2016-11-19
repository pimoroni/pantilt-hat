#Pan-Tilt HAT

Pan-Tilt HAT is a two-channel servo driver designed to control a tiny servo-powered Pan/Tilt assembly. It also controls either PWM-dimmed lights or WS2812 pixels; up to 24 RGB or 18 RGBW.

##Installation

**Full install ( recommended ):**

We've created a super-easy installation script that will install all pre-requisites and get your HAT up and running in a jiffy. To run it fire up Terminal which you'll find in Menu -> Accessories -> Terminal on your Raspberry Pi desktop like so:

![Finding the terminal](terminal.jpg)

In the new terminal window type:

```bash
curl -sS https://get.pimoroni.com/pantilthat | bash
```

If you choose to download examples you'll find them in `/home/pi/Pimoroni/pantilthat/`.

**Library install for Python 3:**


```bash
sudo pip3 install pantilthat
```

**Library install for Python 2:**


```bash
sudo pip2 install pantilthat
```

In all cases you will have to enable the i2c bus.
