import configparser
import os

DEFAULT_CONFIG_FILE = 'config.ini'

def get_config_file():
    return os.environ.get('CONFIG_FILE', DEFAULT_CONFIG_FILE)

CONFIG_FILE = get_config_file()

def create_config(config_file=None):
    parser = configparser.ConfigParser()
    parser.read(config_file or CONFIG_FILE)
    return parser


class ConfigInstance:
    def __init__(self):
        self.__config = create_config()

    def connections(self, key):
        return self.__config.get('CONNECTIONS', key)

    def appSettings(self, key):
        return self.__config.get('APPSETTINGS', key)
    
    def logging(self, key):
        return self.__config.get('LOGGING', key)

    @property
    def BATCH_SIZE(self):
        return int(self.appSettings("BATCH_SIZE"))
        

Config = ConfigInstance()
