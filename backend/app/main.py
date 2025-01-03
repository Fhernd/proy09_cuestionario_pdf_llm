from fastapi import FastAPI, File, UploadFile, Form
from pydantic import BaseModel
from typing import List
from fastapi.responses import JSONResponse

app = FastAPI()


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

    pdf_content = await pdf_file.read()

    text_summary = {
        "total_lines": len(text_lines),
        "example_line": text_lines[0] if text_lines else "No lines provided",
    }

    return {
        "filename": pdf_file.filename,
        "content_type": pdf_file.content_type,
        "text_summary": text_summary,
    }
