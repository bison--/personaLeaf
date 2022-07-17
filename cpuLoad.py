import time
import psutil
from inc import colors
from inc.ColorHelper import ColorHelper
from inc.Settings import settings
from nanoleafapi import Nanoleaf

nl = Nanoleaf(settings.get_first_device_ip())

keep_running = True
while keep_running:
    try:
        cpu_load = psutil.cpu_percent() / 100
        print(cpu_load)
        new_color = ColorHelper.lerp_RGB(colors.GREEN, colors.RED, cpu_load)

        #start_hsv = ColorHelper.rgb_to_hsv(colors.GREEN)
        #end_hsv = ColorHelper.rgb_to_hsv(colors.RED)
        #hsv = ColorHelper.lerp_HSV(start_hsv, end_hsv, cpu_load)
        #print(hsv)
        #new_color = ColorHelper.hsv_to_rgb(hsv)
        #print(new_color)

        nl.set_color(new_color)
        time.sleep(1)
    except KeyboardInterrupt as ex:
        print(ex)
        keep_running = False

nl.set_color(colors.WHITE)

