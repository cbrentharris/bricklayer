import platform
import urllib
import subprocess
from progressbar import ProgressBar

class Downloader(object):

    WINDOWS_DOWNLOAD_URL = "http://cache.lego.com/downloads/ldd2.0/installer/setupLDD-PC-4_3_8.exe"
    MAC_DOWNLOAD_URL = "http://cache.lego.com/downloads/ldd2.0/installer/setupLDD-MAC-4_3_8.zip"

    PB = None

    @classmethod
    def download_ldd(cls):
        if platform.system() == "Darwin":
            urllib.urlretrieve(cls.MAC_DOWNLOAD_URL, "ldd.zip", reporthook=cls.download_progress)
        elif platform.system() == "Windows":
            urllib.urlretrieve(cls.WINDOWS_DOWNLOAD_URL, "ldd.exe")
            # subprocess.Popen("ldd.exe")

    @classmethod
    def download_progress(cls, count, block_size, total_size):
        if not cls.PB:
            cls.PB = ProgressBar(maxval=total_size).start()
        cls.PB.update(count * block_size)



class Installer(object):

    @classmethod
    def install(cls):
        pass
