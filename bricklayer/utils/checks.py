import os 
import platform
import subprocess

def ldd_installed():
    cmd = "where" if platform.system() == "Windows" else "which"
    try: 
        subprocess.call([cmd, "Lego Digital Designer"])
        return True
    except: 
        return False
