import json
from nanoleafapi import discovery
from nanoleafapi import Nanoleaf, NanoleafRegistrationError


def test_connection(ip):
    try:
        nl = Nanoleaf(ip)

        info = nl.get_info()
        print(json.dumps(info, indent=4, sort_keys=True))
        print(nl.auth_token)
        return False
    except NanoleafRegistrationError as nre:
        print('no access token.', nre)
        choice = input('Press enter for another try, enter q to quit:')
        if choice == 'q':
            return False

    return True


print('SCANNING')

# discover seems to be for new, not setup devices?
#nanoleaf_dict = discovery.discover_devices(debug=True)
#print(nanoleaf_dict)

keep_running = True
while keep_running:
    keep_running = test_connection("192.168.1.174")
