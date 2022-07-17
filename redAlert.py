import time
from inc import colors
from inc.Settings import settings
from nanoleafapi import Nanoleaf

nl = Nanoleaf(settings.get_first_device_ip())

# set red
nl.set_color(colors.RED)
nl.set_brightness(0)

keep_running = True
while keep_running:
    try:
        nl.set_brightness(100, 2)
        time.sleep(2.1)
        nl.set_brightness(0, 2)
        time.sleep(2.1)
    except KeyboardInterrupt as ex:
        print(ex)
        keep_running = False

nl.set_brightness(75, 3)
nl.set_color(colors.WHITE)
