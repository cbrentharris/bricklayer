from unittest import TestCase
from bricklayer.utils.downloader import Downloader
import mock

class DownloaderTest(TestCase):

    @mock.patch("urllib.urlretrieve")
    @mock.patch("platform.system", return_value="Darwin")
    def test_it_downloads_the_mac_zip(self, mock_system, mock_retrieve):
        Downloader.download_ldd()
        mock_retrieve.assert_called_with(Downloader.MAC_DOWNLOAD_URL, "ldd.zip", reporthook=Downloader.download_progress)

    @mock.patch("urllib.urlretrieve")
    @mock.patch("platform.system", return_value="Windows")
    def test_it_downloads_the_windows_exe(self, mock_system, mock_retrieve):
        Downloader.download_ldd()
        mock_retrieve.assert_called_with(Downloader.WINDOWS_DOWNLOAD_URL, "ldd.exe")
