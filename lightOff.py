from inc.Settings import settings
from nanoleafapi import Nanoleaf

nl = Nanoleaf(settings.get_first_device_ip())
#print(nl.auth_token)
nl.power_off()
