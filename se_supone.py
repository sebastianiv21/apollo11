import os
import pandas as pd
import yaml


def generar_reportes(directorio):
    # Lista para almacenar los DataFrames de cada archivo .log
    dataframes = []

    # Iterar sobre cada archivo en el directorio
    for archivo in os.listdir(directorio):
        if archivo.endswith('.log'):
            ruta_archivo = os.path.join(directorio, archivo)

            # Leer el archivo YAML y convertirlo en DataFrame
            with open(ruta_archivo, 'r') as file:
                data = yaml.safe_load(file)
                df = pd.json_normalize(data)
                dataframes.append(df)

    # Concatenar todos los DataFrames en uno solo
    df_total = pd.concat(dataframes, ignore_index=True)

    # 1. Cantidad de eventos por estado para cada misión
    conteo_eventos_mision = df_total.groupby(['mission', 'device_type', 'device_status']).size().reset_index(name='count')
    conteo_eventos_mision = conteo_eventos_mision.groupby(['mission', 'device_type', 'device_status']).agg({'count': 'sum'}).reset_index()

    # 2. Dispositivo con mayor número de estados 'unknown' por misión
    max_unknown = df_total[df_total['device_status'] == 'unknown'].groupby(['mission', 'device_type']).size().reset_index(name='count')
    dispositivo_max_unknown = max_unknown.loc[max_unknown.groupby('mission')['count'].idxmax()]

    # 3. Cantidad de dispositivos con estado 'killed'
    total_killed = df_total[df_total['device_status'] == 'killed'].shape[0]

    # 4. Porcentajes de datos generados para cada dispositivo y misión
    porcentajes = df_total.groupby(['mission', 'device_type']).size() / len(df_total) * 100

    # Imprimir resultados
    print("1. Cantidad de eventos por estado para cada misión y dispositivo:")
    print(conteo_eventos_mision)

    print("\n2. Dispositivo con mayor número de estados 'unknown' por misión:")
    print(dispositivo_max_unknown)

    print("\n3. Cantidad de dispositivos con estado 'killed':", total_killed)

    print("\n4. Porcentajes de datos generados para cada dispositivo y misión:")
    print(porcentajes)
