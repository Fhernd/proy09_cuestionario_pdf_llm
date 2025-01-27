# Aplicación Backend con FastAPI

Esta es una aplicación backend desarrollada con **FastAPI** que permite responder a preguntas sobre un archivo PDF. Actualmente, se ha probado para consultar sobre los personajes principales de una obra literaria.

## Características

- API desarrollada con **FastAPI**.
- Soporte para análisis y consulta de contenido en archivos PDF.
- Integración con herramientas de **LLM** para procesamiento y generación de respuestas.
- Uso de librerías avanzadas para procesamiento de lenguaje natural y datos.

## Requisitos Previos

Asegúrate de tener instalado:

- Python 3.9 o superior
- pip (gestor de paquetes de Python)
- Acceso al entorno virtual proporcionado (`venv`)

## Instalación

1. Clona este repositorio en tu máquina local.

```bash
git clone https://github.com/Fhernd/proy09_cuestionario_pdf_llm
cd backend
```

2. Crear el ambiente virtual

```bash
python -m venv venv
```

3. Activa el entorno virtual:

```bash
source venv/bin/activate   # En Linux/Mac
venv\Scripts\activate    # En Windows
```

4. Instala las dependencias:

```bash
pip install -r requirements.txt
```

## Ejecución

1. Activa el entorno virtual (si no lo has hecho ya).

2. Ejecuta el servidor:

```bash
fastapi dev app\main.py
```

3. Accede a la documentación interactiva de la API en tu navegador en:

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Dependencias

La aplicación utiliza las siguientes librerías (archivo completo en `requirements.txt`):

- **FastAPI** para crear la API.
- **LangChain** y **Transformers** para la integración con modelos de lenguaje.
- **PyPDF2** para manejo de archivos PDF.
- **SQLAlchemy** para manejar bases de datos.
- **Uvicorn** como servidor ASGI.

## Pruebas

La funcionalidad principal incluye:
- Análisis de contenido en archivos PDF.
- Respuestas a preguntas relacionadas con el contenido.

Pruebas realizadas sobre obras literarias populares para identificar personajes y temas principales.

## Contribuciones

Si deseas contribuir a este proyecto, por favor:

1. Haz un fork del repositorio.
2. Crea una rama nueva para tus cambios.
3. Envía un pull request con una descripción clara de las modificaciones.

## Licencia

Este proyecto está bajo la licencia MIT.

## Autor:

Ingeniero John Ortiz Ordoñez - X: @JohnLrnr
