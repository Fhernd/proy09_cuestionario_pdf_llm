from io import BytesIO

from PyPDF2 import PdfReader
from langchain_community.text_splitters import RecursiveCharacterTextSplitter  # Actualizado
from langchain_community.vectorstores import FAISS  # Actualizado
from langchain_community.embeddings import HuggingFaceEmbeddings  # Actualizado


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


def particionar_texto_partes(texto, tamanio_parte=1000, parte_empate=200):
    """
    Particiona un texto en partes más pequeñas.

    Args:
    texto (str): El texto a particionar.
    tamanio_parte (int): El tamaño de cada parte.
    parte_empate (int): La cantidad de caracteres que se superponen entre cada parte.

    Returns:
    List[str]: Una lista con las partes del texto.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=tamanio_parte, chunk_overlap=parte_empate
    )
    return splitter.split_text(texto)


def crear_base_conocimiento(partes):
    """
    Crea una base de conocimiento a partir de las partes de un texto.
    
    Args:
    partes (List[str]): Las partes del texto.

    Returns:
    FAISS: La base de conocimiento.
    """
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    knowledge_base = FAISS.from_texts(partes, embeddings)
    return knowledge_base
