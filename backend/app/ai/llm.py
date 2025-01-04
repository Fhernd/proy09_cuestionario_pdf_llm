from langchain.llms import GPT4All


def inicializar_llm(ruta_modelo="models/gpt4all-lora-quantized.bin"):
    """
    Inicializa un modelo de lenguaje.

    Args:
    ruta_modelo (str): La ruta del modelo a cargar.

    Returns:
    GPT4All: El modelo de lenguaje.
    """
    return GPT4All(model=ruta_modelo, n_ctx=512)


def preguntar(base_conocimiento, llm, pregunta):
    """
    Responde una pregunta basada en un contexto proporcionado.

    Args:
    base_conocimiento (DocumentIndex): El índice de documentos.
    llm (GPT4All): El modelo de lenguaje.
    pregunta (str): La pregunta a responder

    Returns:
    str: La respuesta generada por el modelo.
    """

    relevant_docs = base_conocimiento.similarity_search(pregunta, k=4)
    context = " ".join([doc.page_content for doc in relevant_docs])

    prompt = f"""
    Contexto del libro:
    {context}

    Pregunta del usuario:
    {pregunta}

    Responde de manera clara y concisa basada únicamente en el contexto proporcionado.
    """
    
    response = llm(prompt)
    return response.strip()
