import subprocess
import time
import os, config
from api import *

positive = ['yes', 'YES', 'Yes', 'SI', 'si', 'y', 'Y', 's', 'S']
negative = ['No', 'n', 'N', 'NO', 'no']

def run_command(command, description, wait=True):
    """
    Ejecuta un comando del sistema y muestra su salida.
    """
    print(f"{description}")
    try:
        if wait:
            choise = input('Continuar? [Yes(y)]/[No(n)]')
        else:
            choise = 'y'
        if choise in positive:
            result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(result.stdout.decode())
        elif choise in negative:
            #exit(1)
            pass
        os.system(cmd)
    except subprocess.CalledProcessError as e:
        print(f"Error ejecutando: {command}")
        print(e.stderr.decode())
        exit(1)

