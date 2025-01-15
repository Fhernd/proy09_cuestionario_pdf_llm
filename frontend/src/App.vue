<template>
  <div class="max-w-2xl mx-auto p-6">
    <h1 class="text-center text-4xl font-bold text-red-500 bg-yellow-200 p-4 rounded-lg shadow-lg mb-5">Pregunta a la API</h1>
    <SubidaArchivo @file-selected="handleFileUpload" />
    <ListaPreguntas v-model="questions" />
    <button
      @click="submitQuestions"
      class="bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600 mt-4 w-full"
    >
      Preguntar
    </button>
    <div v-if="responses.length" class="mt-6">
      <h2 class="text-xl font-bold mb-4">Respuestas:</h2>
      <ul>
        <li
          v-for="(response, index) in responses"
          :key="index"
          class="mb-2 p-2 border border-gray-300 rounded"
        >
          <strong>Pregunta {{ index + 1 }}:</strong> {{ response.question }}
          <br />
          <strong>Respuesta:</strong> {{ response.answer }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import SubidaArchivo from "./components/SubidaArchivo.vue";
import ListaPreguntas from "./components/ListaPreguntas.vue";
import axios from "axios";

export default {
  components: { SubidaArchivo, ListaPreguntas },
  data() {
    return {
      questions: [""],
      selectedFile: null,
      responses: [],
    };
  },
  methods: {
    handleFileUpload(file) {
      this.selectedFile = file;
    },
    async submitQuestions() {
      if (this.questions.some((q) => !q.trim())) {
        alert("Todos los campos deben contener una pregunta.");
        return;
      }

      if (!this.selectedFile) {
        alert("Debes seleccionar un archivo PDF.");
        return;
      }

      const formData = new FormData();
      formData.append("file", this.selectedFile);
      formData.append("questions", JSON.stringify(this.questions));

      try {
        const { data } = await axios.post(
          "http://localhost:5000/api/questions",
          formData,
          {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          }
        );
        this.responses = data.responses;
      } catch (error) {
        console.error("Error al enviar las preguntas:", error);
        alert("Ocurrió un error al procesar las preguntas.");
      }
    },
  },
};
</script>

<style scoped>
.titulo {
  text-align: center;
  color: #ff6347; /* Tomate */
  background-color: #f0e68c; /* Amarillo claro */
  padding: 10px;
  border-radius: 5px;
}
</style>
