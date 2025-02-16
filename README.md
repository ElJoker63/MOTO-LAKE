# ROM Flasher Tool

Este proyecto es una herramienta para facilitar la instalación de ROMs personalizadas, específicamente LineageOS, en dispositivos Android. Automatiza varios pasos del proceso de flasheo, incluyendo la descarga de archivos necesarios, flasheo de particiones y la instalación de GApps y Magisk.

## Características

*   **Descarga automática de archivos**: Descarga ADB, Fastboot, TWRP, Magisk y los archivos específicos de la ROM (boot, vendor, dtbo, ROM).
*   **Flasheo automatizado**: Reinicia el dispositivo en modo bootloader y recovery, flashea las particiones necesarias (boot, vendor, etc.).
*   **Instalación de GApps y Magisk**: Facilita la instalación de GApps y Magisk a través de sideload.

## Requisitos

*   Python 3.6 o superior
*   ADB y Fastboot instalados (la herramienta los descarga automáticamente si no están presentes)
*   Dispositivo Android con bootloader desbloqueado
*   Drivers ADB instalados en tu PC
*   Las dependencias de Python listadas en `requirements.txt`

## Instalación

1.  Clonar el repositorio:

    ```bash
    git clone https://github.com/ElJoker63/MOTO-LAKE.git
    cd MOTO-LAKE
    ```

2.  Crear un entorno virtual (opcional pero recomendado):

    ```bash
    python3 -m venv venv
    venv\Scripts\activate.bat  # En Windows
    ```

3.  Instalar las dependencias:

    ```bash
    pip install -r requirements.txt
    ```
    Si no existe el archivo `requirements.txt`, instalar las dependencias manualmente:
    ```bash
    pip install wget humanize requests flet adb-shell
    ```

## Uso

El proyecto se puede ejecutar de dos maneras:

### Interfaz de consola

1. Ejecutar el script principal:
    ```bash
    python inter.py
    ```
2.  La herramienta te guiará a través de los pasos necesarios.

### Interfaz gráfica (Flet)

1. Ejecutar el script Flet:

    ```bash
    python test.py
    ```

2.  La interfaz gráfica te guiará a través de los pasos.

### Pasos generales

1.  **Verificar dependencias**: La herramienta descargará automáticamente ADB, Fastboot, TWRP, Magisk y el script para particionar.
2.  **Seleccionar la versión de LineageOS**: La herramienta listará las versiones disponibles para descargar.
3.  **Iniciar la instalación**: La herramienta reiniciará el dispositivo en modo bootloader, flasheará el archivo boot.img, reiniciará en modo recovery, instalará el script para particionar, reiniciará nuevamente en modo recovery e instalará la ROM y las GApps.

## Estructura del proyecto

```
├── adb-fastboot/              # Directorio para ADB y Fastboot
├── partition/                 # Directorio para el script de particiones
├── releases/                  # Directorio para las ROMs descargadas
├── config.py                  # Archivo de configuración
├── api.py                     # Funciones relacionadas con la descarga de archivos y el acceso a la API
├── down.py                    # Funciones relacionadas con la descarga de ROMs y Magisk
├── flash_lineage.py           # Funciones para flashear la ROM
├── requirements.txt           # Lista de dependencias de Python
└── README.md                  # Este archivo
```

## Configuración (config.py)

El archivo `config.py` contiene las siguientes variables de configuración:

*   `ADB`: Directorio donde se guardan ADB y Fastboot.
*   `PARTITION`: Directorio donde se guarda el script de particiones.
*   `PAT`: Nombre del archivo ZIP del script de particiones.
*   `GAPPS`: Nombre del archivo ZIP de GApps.
*   `MAGISK`: Nombre del archivo APK de Magisk.
*   `REPO_MAGISK`: URL de la API de GitHub para obtener la última versión de Magisk.
*   `TWRPURL`: URL para descargar la imagen TWRP.
*   `TWRP`: Nombre del archivo de la imagen TWRP.

## Consideraciones

*   Esta herramienta está diseñada para un dispositivo específico (lake). Es posible que necesites modificarla para otros dispositivos.
*   El proceso de flasheo puede ser peligroso. Asegúrate de entender los riesgos antes de continuar.
*   Siempre haz un backup de tus datos antes de flashear una ROM.
*   Esta herramienta utiliza `adb-shell` para interactuar con el dispositivo mediante ADB. Es posible que debas configurar la autorización ADB si es la primera vez que usas `adb-shell` en tu PC.

## Librerias usadas
*   `wget` - para descargar archivos.
*   `humanize` - para mostrar el tamaño de los archivos.
*   `requests` - para hacer peticiones a la API de Github.
*   `adb-shell` - para interactuar con el dispositivo mediante ADB.
*   `fastboot` - para interactuar con el dispositivo mediante fastboot (esta librería no requiere instalación, es un módulo creado en el proyecto).

## Licencia

Este proyecto tiene licencia MIT.

## Contribuciones

Las contribuciones son bienvenidas.

```