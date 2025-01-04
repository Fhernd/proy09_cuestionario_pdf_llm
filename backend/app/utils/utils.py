from io import BytesIO

from PyPDF2 import PdfReader


def es_pdf_valido(tipo_contenido: str) -> bool:
    """
    Valida si el archivo es un PDF.

    Args:
    tipo_contenido (str): El tipo de contenido del archivo.

    Returns:
    bool: True si el archivo es un PDF, False en caso contrario.
    """
    return tipo_contenido == "application/pdf"


def extraer_texto_desde_pdf(pdf: bytes) -> str:
    """
    Extrae el texto de un archivo PDF.

    Args:
    pdf (bytes): El contenido del archivo PDF.

    Returns:
    str: El texto extraído del archivo
    """
    try:
        pdf_reader = PdfReader(BytesIO(pdf))
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        
        return text
    except Exception as e:
        raise ValueError(f"Error al leer el PDF: {e}")
