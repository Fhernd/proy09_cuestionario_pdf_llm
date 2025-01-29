
# Proyecto Cuestionario sobre Archivos PDF

Esta es una aplicación completa que combina un **frontend desarrollado en Vue.js 3** y un **backend desarrollado en FastAPI**. La aplicación permite analizar el contenido de archivos PDF y responder preguntas basadas en el mismo. Ha sido probada con obras literarias para identificar personajes principales y temas relevantes.

## Características Principales

- **Frontend**:
  - Interfaz desarrollada con Vue.js 3.
  - Funcionalidad de búsqueda y consulta.
  - Diseño responsive para adaptarse a diferentes dispositivos.

- **Backend**:
  - API creada con FastAPI.
  - Procesamiento avanzado de archivos PDF.
  - Integración con modelos de lenguaje natural (LLM).
  - Documentación interactiva con Swagger UI y Redoc.

## Instalación y Ejecución

### Frontend

1. Clona el repositorio e ingresa al directorio del frontend:
   ```bash
   git clone https://github.com/Fhernd/proy09_cuestionario_pdf_llm
   cd frontend
   ```

2. Instala las dependencias:
   ```bash
   npm install
   ```

3. Ejecuta el proyecto en modo desarrollo:
   ```bash
   npm run dev
   ```

4. Compila el proyecto para producción:
   ```bash
   npm run build
   ```

### Backend

1. Clona el repositorio e ingresa al directorio del backend:
   ```bash
   git clone https://github.com/Fhernd/proy09_cuestionario_pdf_llm
   cd backend
   ```

2. Crea y activa un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate   # En Linux/Mac
   venv\Scripts\activate    # En Windows
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Ejecuta el servidor:
   ```bash
   uvicorn app.main:app --reload
   ```

5. Accede a la documentación de la API:
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Dependencias Principales

- **Frontend**:
  - Vue.js 3
  - npm para gestión de paquetes.

- **Backend**:
  - FastAPI
  - LangChain y Transformers para procesamiento de lenguaje natural.
  - PyPDF2 para manejo de PDFs.
  - SQLAlchemy para bases de datos.
  - Uvicorn como servidor ASGI.

## Autor

Este proyecto fue desarrollado por el **Ingeniero John Ortiz Ordoñez**.  
Si tienes preguntas o sugerencias, no dudes en contactarlo en X: [@JohnLrnr](https://x.com/JohnLrnr).

---

¡Gracias por usar este proyecto!
