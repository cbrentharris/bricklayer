import platform
import urllib
import subprocess

class Downloader(object):

    WINDOWS_DOWNLOAD_URL = "http://cache.lego.com/downloads/ldd2.0/installer/setupLDD-PC-4_3_8.exe"
    MAC_DOWNLOAD_URL = "http://cache.lego.com/downloads/ldd2.0/installer/setupLDD-MAC-4_3_8.zip"

    @classmethod
    def download_ldd(cls):
        if platform.system() == "Darwin":
            urllib.urlretrieve(cls.MAC_DOWNLOAD_URL, "ldd.zip")
        elif platform.system() == "Windows":
            urllib.urlretrieve(cls.WINDOWS_DOWNLOAD_URL, "ldd.exe")
            # subprocess.Popen("ldd.exe")


