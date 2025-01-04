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


def ask_question(knowledge_base, llm, user_question):
    """Realiza una pregunta al LLM basada en fragmentos relevantes."""
    # Buscar fragmentos relevantes en el índice
    relevant_docs = knowledge_base.similarity_search(user_question, k=4)
    context = " ".join([doc.page_content for doc in relevant_docs])

    # Crear el prompt para el LLM
    prompt = f"""
    Contexto del libro:
    {context}

    Pregunta del usuario:
    {user_question}

    Responde de manera clara y concisa basada únicamente en el contexto proporcionado.
    """
    # Generar respuesta
    response = llm(prompt)
    return response.strip()
