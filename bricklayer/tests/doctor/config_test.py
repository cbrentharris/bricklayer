from unittest import TestCase
from bricklayer.doctor.config import Configurator
import uuid
import os
import shutil
import tempfile
import ConfigParser

class ConfiguratorTest(TestCase):

    def setUp(self):
        self.random_dir = tempfile.gettempdir()  + '/.' + uuid.uuid4().hex
        os.makedirs(self.random_dir)

    def tearDown(self):
        if self.random_dir is not None:
            shutil.rmtree(self.random_dir)

    def test_it_creates_a_parser(self):
        parser = Configurator.generate_parser()
        self.assertIsNotNone(parser)
        
    def test_it_creates_a_config_file_with_a_uuid_if_one_doesnt_exist(self):
        os.chdir(self.random_dir)
        Configurator.create_config_if_doesnt_exist()
        self.assertTrue(os.path.exists(self.random_dir + '/.bricklayer' + '/settings.cfg'))

    def test_it_adds_the_uuid_to_the_config_file(self):
        os.chdir(self.random_dir)
        Configurator.create_config_if_doesnt_exist()
        config = ConfigParser.RawConfigParser()
        config.read([self.random_dir + '/.bricklayer/settings.cfg'])
        self.assertIsInstance(config.get('General', 'uuid'), str)

    def test_it_doesnt_overwrite_the_config_file(self):
        os.chdir(self.random_dir)
        Configurator.create_config_if_doesnt_exist()
        config = ConfigParser.RawConfigParser()
        config.read([self.random_dir + '/.bricklayer/settings.cfg'])
        generated_uuid = config.get('General', 'uuid')
        Configurator.create_config_if_doesnt_exist()
        config2 = ConfigParser.RawConfigParser()
        config2.read([self.random_dir + '/.bricklayer/settings.cfg'])
        self.assertEqual(generated_uuid, config.get('General', 'uuid'))

