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
