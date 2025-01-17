import apiClient from "@/api/apiClient";

/**
 * Servicio para enviar preguntas y un archivo PDF a la API.
 *
 * @param {File} pdfFile - El archivo PDF que contiene el contenido a analizar.
 * @param {Array<string>} questions - Las preguntas que deseas hacer basadas en el contenido del PDF.
 * @returns {Promise<Object>} Respuestas de la API en formato de objeto.
 * @throws {Error} Si ocurre algún problema al interactuar con la API.
 */
export async function preguntarServicio(pdfFile, questions) {
  const formData = new FormData();
  formData.append("pdf_file", pdfFile);
  formData.append("text_lines", JSON.stringify(questions));

  try {
    const response = await apiClient.post("/preguntar/", formData, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    });

    return response.data;
  } catch (error) {
    console.error("Error al interactuar con la API:", error);
    throw error;
  }
}
