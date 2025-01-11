from fastapi import FastAPI, File, UploadFile, Form
from typing import List
from fastapi.responses import JSONResponse

from .utils.utils import crear_base_conocimiento, es_pdf_valido, extraer_texto_desde_pdf, particionar_texto_partes
from .ai.llm import inicializar_llm, preguntar

app = FastAPI()

llm = None
# llm = inicializar_llm()
knowledge_base = None


@app.get("/")
def home():
    """
    Ruta de inicio de la API.

    Returns:
    Dict[str, str]: Un diccionario con un mensaje de bienvenida.
    """
    return {'mensaje': 'Bienvenido a la API de PDF LLM'}


@app.post("/preguntar/")
async def preguntar_post(
    pdf_file: UploadFile = File(...),
    text_lines: List[str] = Form(...)
):
    """
    Responde preguntas basadas en un archivo PDF.

    Args:
    pdf_file (UploadFile): El archivo PDF con el contenido.
    text_lines (List[str]): Las preguntas a responder.

    Returns:
    Dict[str, str]: Un diccionario con las respuestas a las preguntas.
    """
    if not es_pdf_valido(pdf_file.content_type):
        return JSONResponse(
            status_code=400, content={"error": "Sólo se permiten archivos PDF"}
        )
    global knowledge_base

    llm = inicializar_llm()
    print('ANTES del leer el PDF')
    pdf_content = await pdf_file.read()
    texto_pdf = extraer_texto_desde_pdf(pdf_content)
    print('DESPUÉS del leer el PDF')
    partes = particionar_texto_partes(texto_pdf)
    base_conocimiento = crear_base_conocimiento(partes)
    print('DESPUÉS DEL PARTICIONAMIENTO')
    preguntas = text_lines[0].split(',')
    respuestas = {}

    for p in preguntas:
        respuesta = preguntar(base_conocimiento, llm, p)
        respuestas[p] = respuesta

    return respuestas
