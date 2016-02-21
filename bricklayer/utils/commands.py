import platform

def open_ldd_command(filename):
    if platform.system() == "Darwin":
        return ["open", "-W", filename]
    elif platform.system() == "Windows":
        return ["start", "/wait", filename]

