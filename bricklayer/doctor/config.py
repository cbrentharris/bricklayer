import os
import tempfile
import ConfigParser
import uuid


class Configurator(object):
    @classmethod
    def create_config_if_doesnt_exist(cls):
        u"""
        For bricklayer, there are certain settings necessary to perform certain functions.
        For example, we would like the end user to be able to control what their bricklayer API
        endpoint is they would like to collect metrics to. We would also like to keep track of a
        UUID we can associate the user with without any PII.
        """

        # First, check if the current '.bricklayer' directory exists in CWD
        if os.path.isdir(os.getcwd() + '/.bricklayer'):
            bricklayer_config_path = os.getcwd() + '/.bricklayer'
        # Next, check if our temp dir has a '.bricklayer' directory
        elif os.path.isdir(tempfile.gettempdir() + '/.bricklayer'):
            bricklayer_config_path = tempfile.gettempdir() + '/.bricklayer'
        # If we can create the config dir in our CWD, do it.
        elif os.access(os.getcwd(), os.W_OK):
            bricklayer_config_path = os.getcwd() + '/.bricklayer'
            os.makedirs(bricklayer_config_path)
        # Last, create the config dir the tempdir.
        else:
            bricklayer_config_path = tempfile.gettempdir() + '/.bricklayer'
            os.makedirs(bricklayer_config_path)
        cls.bricklayer_settings_filename = bricklayer_config_path + '/settings.cfg'
        # We will use a 'settings.cfg' to keep track of settings
        if not os.path.exists(bricklayer_config_path + '/settings.cfg'):
            config = ConfigParser.RawConfigParser()
            config.add_section('General')
            config.set('General', 'uuid', str(uuid.uuid4()))
            with open(bricklayer_config_path + '/settings.cfg', 'w+') as configfile:
                config.write(configfile)

    @classmethod
    def set(cls, key, value):
        cls.create_config_if_doesnt_exist()
        config = ConfigParser.ConfigParser()
        config.read([cls.bricklayer_settings_filename])
        config.set('General', key, value)
        with open(cls.bricklayer_settings_filename, 'wb') as configfile:
            config.write(configfile)

    @classmethod
    def get(cls, key):
        cls.create_config_if_doesnt_exist()
        config = ConfigParser.ConfigParser()
        config.read([cls.bricklayer_settings_filename])
        return config.get('General', key)
