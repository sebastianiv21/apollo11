import random
import yaml
from datetime import datetime


def generar_nombre_archivo(mission_code, num):
    """
    Genera el nombre de un archivo basado en el código de misión y un número.

    Parameters:
    - mission_code (str): Código de la misión.
    - num (int): Número del archivo.

    Returns:
    str: Nombre del archivo generado.
    """
    try:
        return f"APL[{mission_code}]-0000{num:03d}.log"
    except Exception as e:
        print(f"Error al generar el nombre del archivo: {e}")
        raise


def generar_estado_dispositivo():
    """
    Genera un estado aleatorio para un dispositivo.

    Returns:
    str: Estado aleatorio del dispositivo.
    """
    try:
        estados = ['excelente', 'bueno', 'advertencia',
                   'defectuoso', 'inoperable', 'desconocido']
        return random.choice(estados)
    except Exception as e:
        print(f"Error al generar el estado del dispositivo: {e}")
        raise


def obtener_nombre_mision(mission_code):
    """
    Obtiene el nombre de la misión basado en el código.

    Parameters:
    - mission_code (str): Código de la misión.

    Returns:
    str: Nombre de la misión.
    """
    try:
        misiones = {
            'ORBONE': 'OrbitOne',
            'CLNM': 'ColonyMoon',
            'TMRS': 'VacMars',
            'GALXONE': 'GalaxyTwo',
            'UNKN': 'UNKN'
        }
        return misiones.get(mission_code, 'Unknown')
    except Exception as e:
        print(f"Error al obtener el nombre de la misión: {e}")
        raise


def generar_contenido_archivo(mission_code, num):
    """
    Genera el contenido de un archivo YAML con datos aleatorios.

    Parameters:
    - mission_code (str): Código de la misión.
    - num (int): Número del archivo.

    Returns:
    str: Contenido del archivo en formato YAML.
    """
    try:
        fecha_actual = datetime.now().strftime('%d%m%Y%H%M%S')

        if mission_code == 'UNKN':
            data = {
                'date': fecha_actual,
                'mission': obtener_nombre_mision(mission_code),
                'device_type': 'Unknown',
                'device_status': 'Unknown',
                'hash': 'Unknown',
                'random_number': 'Unknown'
            }
        else:
            device_type = f"Device_{num}"
            device_status = generar_estado_dispositivo()
            hash_value = hash(
                f"{mission_code}{fecha_actual}{device_type}{device_status}")

            data = {
                'date': fecha_actual,
                'mission': obtener_nombre_mision(mission_code),
                'device_type': device_type,
                'device_status': device_status,
                'hash': hash_value,
            }

        return yaml.dump(data, default_flow_style=False)
    except Exception as e:
        print(f"Error al generar el contenido del archivo: {e}")
        raise


def generar_archivos_mision(num_archivos):
    """
    Genera archivos de misiones con datos aleatorios.

    Parameters:
    - num_archivos (int): Número de archivos a generar.
    """
    try:
        for i in range(1, num_archivos + 1):
            mission_code = random.choice(
                ['ORBONE', 'CLNM', 'TMRS', 'GALXONE', 'UNKN'])
            nombre_archivo = generar_nombre_archivo(mission_code, i)
            contenido_archivo = generar_contenido_archivo(mission_code, i)

            with open(nombre_archivo, 'w') as file:
                file.write(contenido_archivo)
    except Exception as e:
        print(f"Error al generar archivos de misiones: {e}")
        raise


if __name__ == "__main__":
    """
    Punto de entrada principal del script.
    """
    try:
        num_archivos = random.randint(1, 100)
        generar_archivos_mision(num_archivos)
    except Exception as e:
        print(f"Error en la ejecución del programa: {e}")
