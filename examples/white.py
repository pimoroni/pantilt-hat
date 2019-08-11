#!/usr/bin/env python

import pantilthat


pantilthat.light_mode(pantilthat.WS2812)
pantilthat.light_type(pantilthat.GRBW)
pantilthat.set_all(0, 0, 0, 255)
pantilthat.show()
