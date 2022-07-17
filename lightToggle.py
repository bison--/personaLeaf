from inc.Settings import settings
from nanoleafapi import Nanoleaf

nl = Nanoleaf(settings.get_first_device_ip())
nl.toggle_power()
