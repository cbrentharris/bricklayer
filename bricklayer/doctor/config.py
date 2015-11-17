import argparse
import os
import tempfile
import ConfigParser
import uuid

class Configurator(object):

    @staticmethod
    def create_config_if_doesnt_exist():
        u"""
        For bricklayer, there are certain settings necessary to perform certain functions.
        For example, we would like the end user to be able to control what their bricklayer API
        endpoint is they would like to collect metrics to. We would also like to keep track of a
        UUID we can associate the user with without any PII.
        """
        bricklayer_config_path = None
        # First, try to write to the current directory.
        if not os.path.isdir(os.getcwd() + '/.bricklayer') and os.access(os.getcwd(), os.W_OK):
            bricklayer_config_path = os.getcwd() + '/.bricklayer'
            os.makedirs(bricklayer_config_path)
        # Next, try to write to the temp dir.
        elif not os.path.isdir(os.getcwd() + '/.bricklayer') and os.access(tempfile.gettempdir(), os.W_OK) and not os.path.isdir(tempfile.gettempdir() + '/.bricklayer'):
            bricklayer_config_path = tempfile.gettempdir() + '/.bricklayer'
            os.makedirs(bricklayer_config_path)
        if bricklayer_config_path is not None:
            # We will use a 'settings.cfg' to keep track of settings
            if not os.path.exists(bricklayer_config_path + '/settings.cfg'):
                config = ConfigParser.RawConfigParser()
                config.add_section('General')
                config.set('General', 'uuid', str(uuid.uuid4())) 
                with open(bricklayer_config_path + '/settings.cfg', 'w+') as configfile:
                    config.write(configfile)

    @staticmethod
    def generate_parser():
        description = """
        The doctor module will tell you what might be wrong with your bricklayer program. 
        It also will collect metrics about your programs to allow you to track your progress.
        """
        parser = argparse.ArgumentParser()
        return parser
