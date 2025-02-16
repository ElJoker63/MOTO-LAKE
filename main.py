from down import search_release, versiones, download_magisk, download_twrp
from flash_lineage import run_command
from api import install_adb_fastboot, download_partitioner
import os
import json
from config import *

fastboot = os.path.join(ADB, 'fastboot.exe')
adb = os.path.join(ADB, 'adb.exe')
partition = os.path.join(PARTITION, PAT)

def install_rom(boot, rom, gapps, vendor, magisk):
    run_command(f"{adb} -d reboot bootloader", "Reiniciando en modo bootloader...")
    run_command(f"{fastboot} flash boot {boot}", "Flasheando el archivo boot.img...")
    run_command(f"{fastboot} reboot recovery", "Reiniciando en modo recovery...")
    run_command(f"{adb} -d sideload {partition}", f"Instalando el archivo {PAT}...")
    run_command(f"{adb} -d reboot recovery", "Reiniciando en modo recovery...")
    run_command(f"{adb} -d sideload {rom}", f"Instalando la ROM desde {rom}...")
    run_command(f"{adb} -d reboot bootloader", "Reiniciar en modo bootloader...")
    run_command(f"{fastboot} erase userdata", "Eliminar USERDATA")
    run_command(f"{fastboot} boot {TWRP}", "Iniciar TWRP")
    print(f"Continue en la pantalla de su dispositivo")
    run_command(f"{adb} push {gapps} /sdcard/{gapps}", f"Subir {gapps}...")
    run_command(f"{adb} push {magisk} /sdcard/{magisk.replace('apk', 'zip')}", f"Subir {magisk.replace('apk', 'zip')}...", wait=False)
    print(f"Instale {gapps} y {magisk} desde TWRP")
    run_command(f"{adb} -d reboot", "Reiniciar normal...")
    print(f"Active la Depuracion USB")
    run_command(f"adbe install {magisk}", f"Instalar {magisk}")
    run_command(f"adbe start com.topjohnwu.magisk", f"Iniciar Magisk")
    run_command(f"adbe push {magisk} /sdcard/{magisk}", f"Subir {magisk}...")
    print(f"\nProceso completado.\nLa ROM {rom} y las GApps deberían estar instaladas.")

def main():
    if not os.path.exists(ADB):
        install_adb_fastboot()
    if not os.path.exists(PARTITION):
        download_partitioner()
    if not os.path.exists(MAGISK):
        download_magisk()
    if not os.path.exists(TWRP):
        download_twrp()
    ver = versiones()
    for version in ver:
        print(f"  [-]{version}")
    files = search_release(input(">>> "))
    data = json.loads(files)
    install_rom(data['boot'], data['rom'], GAPPS, data['vendor'], MAGISK)
    
if __name__ == "__main__":
    main()