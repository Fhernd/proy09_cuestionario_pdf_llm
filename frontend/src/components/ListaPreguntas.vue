<template>
  <div>
    <div v-for="(question, index) in questions" :key="index">
      <PreguntaInput v-model="questions[index]" @remove="removeQuestion(index)" @pregunta-cambiada="cambiarPregunta"/>
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
    cambiarPregunta(pregunta) {
      this.$emit("pregunta-cambiada", this.questions);
    },
  },
};
</script>