import os
from typing import Optional


def crear_carpeta_devices(ruta: str, nombre: Optional[str] = 'devices') -> str:
    """
    Crea una carpeta llamada 'devices' en la ruta especificada.
    Parámetros:
    - ruta (str): La ruta en la que se creará la carpeta.
    - nombre (str, opcional): El nombre de la carpeta a crear.
        Por defecto, 'devices'.
    Retorna:
    - str: La ruta completa de la carpeta creada.
    """
    # Combinar la ruta y el nombre de la carpeta
    ruta_carpeta = os.path.join(ruta, nombre)

    # Crear la carpeta si no existe
    if not os.path.exists(ruta_carpeta):
        os.makedirs(ruta_carpeta)

    return ruta_carpeta


crear_carpeta_devices('proyecto')
