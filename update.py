import requests
import os
import subprocess
import ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def download_run_patch_my_pc():
    url = 'https://patchmypc.com/freeupdater/PatchMyPC.exe'
    r = requests.get(url)
    if is_admin():
        open('PatchMyPC.exe', 'wb').write(r.content)
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    subprocess.call(['PatchMyPC.exe'])

if __name__ == "__main__":
    download_run_patch_my_pc()