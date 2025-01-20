<template>
  <div>
    <div v-for="(question, index) in questions" :key="index">
      <PreguntaInput @remove="removeQuestion" @pregunta-cambiada="cambiarPregunta"
      :question="question" :index="index"
      />
    </div>
    <button @click="addQuestion" class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 mb-4 w-full">
      <i class="fas fa-plus"></i> Agregar pregunta
    </button>
  </div>
</template>

<script>
import PreguntaInput from "./PreguntaInput.vue";

export default {
  components: { PreguntaInput },
  props: ["value"],
  data() {
    return {
      questions: this.value || [""],
    };
  },
  watch: {
    questions: {
      deep: true,
      handler(newVal) {
        this.$emit("update:value", newVal);
      },
    },
  },
  methods: {
    addQuestion() {
      this.questions.push("");
    },
    removeQuestion(index) {
      this.questions.splice(index, 1);
    },
    cambiarPregunta(index, pregunta) {
      console.log("ListaPreguntas > cambiarPersona > index", index);
      console.log("ListaPreguntas > cambiarPersona > pregunta", pregunta);
      console.log();
      
      this.$emit("pregunta-cambiada", this.questions);
    },
  },
};
</script>