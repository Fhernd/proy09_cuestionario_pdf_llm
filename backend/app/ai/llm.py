from langchain_community.llms import GPT4All


def inicializar_llm():
    """
    Inicializa un modelo de lenguaje.

    Args:
    ruta_modelo (str): La ruta del modelo a cargar.

    Returns:
    GPT4All: El modelo de lenguaje.
    """
    model_path=r'E:\Dev\proy09_cuestionario_pdf_llm\backend\llms'
    print('model_path:', model_path)
    return GPT4All(model='orca-mini-3b-gguf2-q4_0.gguf')


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
