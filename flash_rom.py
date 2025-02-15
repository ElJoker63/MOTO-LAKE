from adb_shell.adb_device import AdbDeviceTcp, AdbDeviceUsb
from adb_shell.auth.sign_pythonrsa import PythonRSASigner
from fastboot import FastbootCommands

def connect_device():
    """
    Conecta con el dispositivo usando ADB.
    """
    try:
        device = AdbDeviceUsb()
        device.connect()
        print("Dispositivo conectado correctamente.")
        return device
    except Exception as e:
        print(f"Error al conectar el dispositivo: {e}")
        exit(1)

def adb_reboot_to_bootloader(device):
    print("Reiniciando en modo bootloader...")
    device.shell("reboot bootloader")

def fastboot_flash_boot(image_path):
    print("Flasheando boot.img...")
    fastboot = FastbootCommands()
    fastboot.connect()
    fastboot.flash_partition("boot", image_path)
    fastboot.close()

def adb_sideload(device, file_path):
    print(f"Instalando {file_path} con sideload...")
    device.shell(f"sideload {file_path}")

def adb_reboot(device, mode):
    print(f"Reiniciando en modo {mode}...")
    device.shell(f"reboot {mode}")

def main():
    # Conexión inicial con el dispositivo
    device = connect_device()

    # Paso 1 - Reiniciar en modo bootloader
    adb_reboot_to_bootloader(device)

    # Paso 2 - Flashear boot.img
    fastboot_flash_boot("boot.img")

    # Paso 3 - Sideload del archivo de particiones
    adb_sideload(device, "copy-partitions-20220613-signed.zip")

    # Paso 4 - Reiniciar en modo recovery
    adb_reboot(device, "recovery")

    # Paso 5 - Sideload del archivo de la ROM
    rom_filename = "filename.zip"  # Cambiar por el nombre real del archivo
    adb_sideload(device, rom_filename)

    # Paso 6 - Reiniciar nuevamente en recovery
    adb_reboot(device, "recovery")

    # Paso 7 - Sideload de GApps
    gapps_filename = "gapps.zip"  # Cambiar por el nombre real del archivo
    adb_sideload(device, gapps_filename)

    print("Proceso de instalación completado correctamente.")

