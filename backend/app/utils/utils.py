def es_pdf_valido(tipo_contenido: str) -> bool:
    """
    Valida si el archivo es un PDF.

    Args:
    tipo_contenido (str): El tipo de contenido del archivo.

    Returns:
    bool: True si el archivo es un PDF, False en caso contrario.
    """
    return tipo_contenido == "application/pdf"
