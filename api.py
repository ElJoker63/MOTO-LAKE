import wget
import os
import humanize
import sys
import platform
from config import *

so = platform.system()
cmd = 'cls' if so == 'Windows' else 'clear'
url = 'https://github.com/K3V1991/ADB-and-FastbootPlusPlus/raw/refs/heads/main/'
files = ['AdbWinApi.dll', 'AdbWinUsbApi.dll', 'adb.exe', 'fastboot.exe']

def download(url, file):
    global filename
    filename = file.split('/')[-1]
    file = wget.download(url=url, out=file, bar=bar_progress)
    return file

def bar_progress(current, total, length=5, width=80):
    filled_length = int(length * current // total)
    bar = "●" * filled_length + "○" * (length - filled_length)
    percentage = round((current / total) * 100, 2)
    text = (f'{filename} |{percentage}% | Processed: {humanize.naturalsize(current)} of {humanize.naturalsize(total)}')
    sys.stdout.write("\r" + text)
    sys.stdout.flush()

def install_adb_fastboot():
    if not os.path.exists(ADB):
        print(f'[+] Instalando ADB y FASTBOOT')
        os.makedirs(ADB)
    for file in files:
        if not os.path.exists(f'{ADB}/{file}'):
            download(f'{url}{file}', f'{ADB}/{file}')
    os.system(cmd)

def download_partitioner():
    url = 'https://mirrorbits.lineageos.org/tools/copy-partitions-20220613-signed.zip'
    file = url.split('/')[-1]
    if not os.path.exists(f'{PARTITION}/{file}'):
        print(f'\n[+] Descargando {file}')
        os.makedirs(PARTITION)
        if not os.path.exists(f'{PARTITION}/{file}'):
            download(f'{url}', f'{PARTITION}/{file}')
    os.system(cmd)