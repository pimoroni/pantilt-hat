#!/usr/bin/env python

import pantilthat


pantilthat.light_mode(pantilthat.WS2812)
pantilthat.light_type(pantilthat.GRBW)
pantilthat.set_all(255, 255, 255, 255)
pantilthat.show()
