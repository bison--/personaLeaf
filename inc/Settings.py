import json


class Settings:
    SETTINGS_FILE_AUTH = 'data/auth.json'
    SETTINGS_FILE_KNOWN_DEVICES = 'data/known_devices.json'

    def __init__(self):
        self.auth_code = ''
        self.device_list = []

        self.load_files()

    def load_files(self):
        try:
            self.load_known_devices()
        except FileNotFoundError:
            print('no known devices')

        try:
            self.load_auth()
        except FileNotFoundError:
            print('not auth file')

    def get_first_device_ip(self):
        return self.device_list[0]['ip']

    def load_known_devices(self):
        self.device_list = json.loads(open(Settings.SETTINGS_FILE_KNOWN_DEVICES).read())

    def load_auth(self):
        auth_code_json = json.loads(open(Settings.SETTINGS_FILE_AUTH).read())
        self.auth_code = auth_code_json['auth-token']


settings = Settings()
