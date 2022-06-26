#!/usr/bin/env python3

import pantilthat


pantilthat.light_mode(pantilthat.WS2812)
pantilthat.light_type(pantilthat.GRBW)
pantilthat.set_all(0, 0, 0, 127)
pantilthat.show()
