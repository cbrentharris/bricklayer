from unittest import TestCase
from bricklayer.utils.commands import open_ldd_command
import platform
import mock

class CommandsTest(TestCase):

    def test_it_creates_the_right_windows_command(self):
        with mock.patch('platform.system',return_value='Windows'):
            self.assertEquals(open_ldd_command("file.txt"), ["start", "/wait", "file.txt"])

    def test_it_creates_the_right_mac_command(self):
        with mock.patch('platform.system',return_value='Darwin'):
            self.assertEquals(open_ldd_command("file.txt"), ["open", "-W", "file.txt"])

