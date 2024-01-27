#### <p align="center">Tabla de Contenido </p>

[Descripción del Proyecto](#descripción-del-proyecto) 

[Objetivo](#objetivo)

[Equipo de especialistas](#💻-equipo-de-especialistas)

[Centro de operaciones](#🏢-centro-de-operaciones-cabo-cañaveral)

[Requerimientos](#📜-requerimientos-del-proyecto)

[Instrucciones de uso](#📜-instrucciones-de-uso)


#  <p align="center"> 🚀 Apollo-11: Sistema de Simulación y Monitoreo para Misiones Espaciales</p>


<p align="center"> <img src="docs/build/html/_static/imageapollo.png" width="300" height="300"> </p>


## <p align="center"> Descripción del Proyecto </p>

Desarrollado por la NASA, este sistema implementa un monitoreo basado en la transmisión de archivos con intervalos de 20 segundos, con el objetivo de proporcionar un control detallado sobre el estado operativo de cada componente clave para detectar tempranamente posibles anomalías. Esto facilita la toma de acciones preventivas tanto en el espacio como en la Tierra.


## <p align="center"> Objetivo </p>

La adopción de esta tecnología avanzada es crucial para asegurar la seguridad de astronautas y turistas en futuras misiones espaciales. Además, la capacidad de monitoreo en tiempo real proporcionada por este sistema ofrece una ventaja significativa, permitiendo una respuesta inmediata ante cualquier situación imprevista. Esto, a su vez, mejora la eficiencia y la efectividad de los siguientes proyectos espaciales:

1. 📡 **OrbitOne**: Modernizar la flota de satélites representa un avance significativo para mejorar el rendimiento y expandir las comunicaciones, no solo optimizando la cobertura, sino también mejorando considerablemente la calidad de las transmisiones y la recopilación de datos.

<p align="center"><img src="docs/build/html/_static/Orbitone.png" width="200" height="200"> </p>


2. 🌕 **ColonyMoon**: Destinado a establecer una colonia lunar, con la finalidad de redefinir de manera significativa la narrativa de la exploración espacial. Más allá de la notoriedad asociada con la presencia humana en nuestro satélite natural, la colonia propuesta se vislumbra como un laboratorio espacial singular para experimentación avanzada, así como una base estratégica para futuras incursiones espaciales más allá de nuestro sistema solar.

<p align="center"><img src="docs/build/html/_static/Colonymoon.png" width="200" height="200"></p>

3. 🌋 **VacMars**: Al hacer que Marte sea accesible para los turistas, se establecería una nueva era de colaboración público-privada en la exploración espacial, creando una sinergia entre los intereses comerciales y la investigación científica.

<p align="center"><img src="docs/build/html/_static/Vacmars.png" width="200" height="200"></p>

4. 🌌 **GalaxyTwo**: La exploración de otras galaxias representa un salto gigantesco en nuestro entendimiento del universo, no solo se centraría en la expansión del conocimiento científico, sino que también podría inspirar nuevas formas de colaboración internacional en la búsqueda de respuestas a las preguntas fundamentales sobre el origen y la naturaleza del cosmos.

<p align="center"><img src="docs/build/html/_static/Galaxytwo.png" width="200" height="200"></p>

## <p align="center"> 💻 Equipo de especialistas </p>

|  Nombres |  Apellidos | Cargo  |
| :------------: | :------------: | :------------: |
| Luis Sebastian  |  Ibarra Villamil | Ingeniero de Sistemas Espaciales  |
| Leonardo Alfonso  |  Cometa Trujillo | Ingeniero de Software Espacial  |
| Alvaro Jose  | Polania Alvarez | Ingeniero de Comunicaciones Espaciales  |

## <p align="center"> 🏢 Centro de operaciones: Cabo Cañaveral </P>

<p align="center"><img src="docs/build/html/_static/Cañaveral.jpg "width="200" height="200"></p>

Ubicado en la costa este de Florida, Estados Unidos, es reconocido por ser la sede del Centro Espacial Kennedy (CEK), una instalación fundamental para la exploración espacial. A lo largo de los años, ha contribuido significativamente al desarrollo de la exploración espacial, siendo crucial en el programa Apolo y en el lanzamiento de misiones del transbordador espacial que facilitaron la construcción y mantenimiento de la Estación Espacial Internacional (EEI). 


## <p align="center"> 📜 Requerimientos del proyecto </P>

### <p align="center"> 1. Instalación de Python </P>

Asegúrese de que su sistema cumpla con los siguientes requisitos antes de comenzar la instalación:

- Conexión a Internet
- Espacio suficiente en disco
- Privilegios de administrador (en caso necesario)

#### Windows

1. Abra su navegador web y visite [python.org](https://www.python.org/).
2. En la sección "Downloads", haga clic en "Python for Windows".
3. Descargue el instalador ejecutable (`*.exe`).

#### macOS

1. Abra su navegador web y visite [python.org](https://www.python.org/).
2. En la sección "Downloads", haga clic en "Python for macOS".
3. Descargue y ejecute el instalador.

#### Linux

La instalación en Linux puede variar según la distribución. A continuación, se muestra un ejemplo para distribuciones basadas en Debian (como Ubuntu):

1. Abra la terminal.
2. Ejecute los siguientes comandos:

```bash
sudo apt update
sudo apt install python3
```

 :memo: **Recomendación:** Elegir la versión de Python que mejor se adapte a sus necesidades, sin embargo se recomienda utilizar la versión más reciente.

### <p align="center"> 1. Instalación de Poetry con Pip </P>

#### Requisitos previos

Antes de comenzar con la instalación, asegúrese de tener Python y Pip instalados en su sistema. Puede verificar su instalación ejecutando los siguientes comandos en la terminal:

```bash
python --version
pip --version
```

Si no tiene pip instalado o necesita actualizarlo, puede hacerlo ejecutando el siguiente comando:
```bash
python -m ensurepip --default-pip
```
##### Paso 1: Instalar Poetry con Pip
Para instalar Poetry, ejecutaremos el siguiente comando en la terminal:

```bash
pip install poetry
```
Este comando descargará e instalará Poetry y sus dependencias. Después de la instalación, puede verificar si Poetry se instaló correctamente ejecutando:

```bash
poetry --version
```
##### Paso 2: Configuración de Poetry
Poetry utiliza un archivo pyproject.toml para gestionar las dependencias y la configuración del proyecto. Para iniciar un nuevo proyecto Poetry o migrar un proyecto existente, navegue hasta el directorio de su proyecto y ejecute:
```bash
poetry init
```
:memo: **Recomendación:** Siga las instrucciones en pantalla para configurar su proyecto. Al finalizar, se generará un archivo pyproject.toml con la información de su proyecto.

##### Paso 3: Crear un entorno virtual
Poetry gestiona las dependencias dentro de un entorno virtual. Para crear un nuevo entorno virtual para su proyecto, ejecute:

```bash
poetry install
```
:memo: **Nota:**Este comando leerá las dependencias de su archivo pyproject.toml y creará un entorno virtual en el directorio .venv.

##### Paso 4: Activar el entorno virtual
Para activar el entorno virtual, utilice el siguiente comando

En sistemas basados en Unix (Linux/Mac):
```bash
source .venv/bin/activate
```
En sistemas Windows:
```bash
.venv\Scripts\activate
```
:memo: **Nota:**Cuando el entorno virtual esté activado, verá el nombre de su entorno en el indicador de la terminal.

## <p align="center"> 📜 Instrucciones de uso </P>

