<template>
  <div class="max-w-2xl mx-auto p-6">
    <h1 class="text-center text-4xl font-bold text-red-500 bg-yellow-200 p-4 rounded-lg shadow-lg mb-5">
      Pregunta a la API
    </h1>
    <SubidaArchivo @file-selected="handleFileUpload" />
    <ListaPreguntas v-model="questions" @pregunta-cambiada="cambiarPregunta" />
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

    <loading v-model:active="isLoading"
                 :can-cancel="true"
                 :on-cancel="onCancel"
                 :is-full-page="true"/>
  </div>
</template>

<script>
import { ref } from "vue";

import Loading from 'vue-loading-overlay';
import 'vue-loading-overlay/dist/css/index.css';

import SubidaArchivo from "./components/SubidaArchivo.vue";
import ListaPreguntas from "./components/ListaPreguntas.vue";
import { preguntarServicio } from "./services/preguntas";

export default {
  components: { SubidaArchivo, ListaPreguntas },
  setup() {
    const questions = ref([""]);
    const selectedFile = ref(null);
    const responses = ref([]);
    const isLoading = ref(false);

    const handleFileUpload = (file) => {
      selectedFile.value = file;
    };

    const cambiarPregunta = (index, pregunta) => {
      questions.value[index] = pregunta;
    };

    const onCancel = () => {
      console.log('onCancel');
      isLoading.value = false;
    };

    const submitQuestions = async () => {
      console.log('questions', questions.value);
      
      if (questions.value.some((q) => !q.trim())) {
        alert("Todos los campos deben contener una pregunta.");
        return;
      }
      
      if (!selectedFile.value) {
        alert("Debes seleccionar un archivo PDF.");
        return;
      }
      
      isLoading.value = true;

      preguntarServicio(selectedFile.value, questions.value)
        .then((res) => {
          console.log('res', res);
          
          isLoading.value = false;
          responses.value = res.data;
        })
        .catch((err) => {
          isLoading.value = false;
          console.error(err);
          alert("Ocurrió un error al enviar las preguntas.");
        });
    };

    return {
      questions,
      selectedFile,
      responses,
      handleFileUpload,
      submitQuestions,
      cambiarPregunta,
      isLoading
    };
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
