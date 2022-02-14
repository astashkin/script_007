import configparser
from src.utils.python_interfaces import Singleton


class Config(metaclass=Singleton):

    def __init__(self):
        self.config_data = None

    def load(self, filename):
        self.config_data = configparser.ConfigParser()
        self.config_data.read(filename)

    def _get_config_value_from_file(self, section, key):
        if not self.config_data:
            return None
        elif section not in self.config_data:
            return None
        elif key not in self.config_data[section]:
            return None
        else:
            return self.config_data[section][key]

    def signature_algo(self):
        config_section = 'Signature'
        config_key = 'signature_algo'
        default_value = 'md5'
        config_file_value = self._get_config_value_from_file(config_section, config_key)
        return config_file_value if config_file_value else default_value

    def signature_dirs(self):
        pass
