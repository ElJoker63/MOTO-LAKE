import requests, json, os
from api import *

def check_releases(url):
    resp = requests.get(url).text
    data = json.loads(resp)
    return data

def download_twrp():
    print(f'[+] Descargando TWRP')
    file = TWRPURL.split('/')[-1]
    twrp = download(TWRPURL, file)
    os.system(cmd)
    return twrp

def download_magisk():
    if os.path.exists(MAGISK):
        print(f'[+] MAGISK ya esta descargado')
        return MAGISK
    else:
        print(f'[+] Descargando MAGISK')
        resp = requests.get(REPO_MAGISK).text
        data = json.loads(resp)
        last = data['assets'][0]
        url = last['browser_download_url']
        file = last['label']
        magisk = download(url, file)
        os.system(cmd)
        return magisk

def versiones():
    print(f'[+] VERSIONES:')
    releases = check_releases('https://api.github.com/repos/ods-releases/lake/releases')
    version = []
    for release in releases:
        version.append(release['tag_name'])
    return version

def download_release(url, name):
    global filename
    filename = url.split('/')[-1]
    file = f'releases/{name}/{filename}'
    if not os.path.exists(f'releases/{name}'):
        os.makedirs(f'releases/{name}')    
    if not os.path.exists(file):
        files = download(url, file)
    else:
        files = file
    return files

def search_release(text):
    print(f'[+] Buscando LineageOS {text} en las releases')
    releases = check_releases('https://api.github.com/repos/ods-releases/lake/releases')
    global url
    lol = []
    files = {
        "boot": None,
        "vendor": None,
        "dtbo": None,
        "rom": None
    }
    for release in releases:
        for last in release['assets']:
            if text in release['tag_name']:
                url = last['browser_download_url']
                name = release['tag_name']
                file = url.split('/')[-1]
                xd = {"url": url, "name": name, "file": file}
                lol.append(xd)
    print(f'[♠] Se encontraron {len(lol)} Archivos')
    for xd in lol:
        print(f'    [♣] Descargando {xd["file"]}')
        file = download_release(xd['url'], xd['name'])
        print(f'\n      [♦] Archivo: {file}')
        if file.split('/')[-1] == 'boot.img':
            files["boot"] = file
        elif file.split('/')[-1] == 'dtbo.img':
            files["dtbo"] = file
        elif file.split('/')[-1] == 'vendor.img':
            files["vendor"] = file
        else:
            files["rom"] = file
    files_json = json.dumps(files, indent=4)
    return files_json

