from fastapi import FastAPI, File, UploadFile, Form
from pydantic import BaseModel
from typing import List
from fastapi.responses import JSONResponse

from .utils.utils import crear_base_conocimiento, es_pdf_valido, extraer_texto_desde_pdf, particionar_texto_partes
from .ai.llm import inicializar_llm, preguntar

app = FastAPI()

llm = inicializar_llm()
knowledge_base = None


@app.get("/")
def home():
    return {'mensaje': 'Bienvenido a la API de PDF LLM'}


@app.post("/preguntar/")
async def preguntar(
    pdf_file: UploadFile = File(...),
    text_lines: List[str] = Form(...)
):
    if pdf_file.content_type != "application/pdf":
        return JSONResponse(
            status_code=400, content={"error": "Sólo se permiten archivos PDF"}
        )
    global knowledge_base

    pdf_content = await pdf_file.read()
    texto_pdf = extraer_texto_desde_pdf(pdf_content)

    partes = particionar_texto_partes(texto_pdf)
    base_conocimiento = crear_base_conocimiento(partes)

    preguntas = text_lines[0].split(',')
    respuestas = {}

    for p in preguntas:
        respuesta = preguntar(base_conocimiento, llm, p)
        respuestas[p] = respuesta

    return respuestas
