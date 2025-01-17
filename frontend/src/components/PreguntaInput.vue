<template>
    <div class="flex items-center gap-2 mb-4">
      <input
        v-model="questionText"
        type="text"
        placeholder="Escribe tu pregunta..."
        class="flex-1 border border-gray-300 rounded px-4 py-2 focus:outline-none focus:ring focus:ring-blue-500"
        @input="validateInput"
      />
      <button
        @click="$emit('remove')"
        class="bg-red-500 text-white px-3 py-2 rounded hover:bg-red-600"
      >
      <i class="fas fa-trash-alt"></i>
      </button>
    </div>
  </template>
  
  <script>
  export default {
    props: ["value"],
    data() {
      return {
        questionText: this.value || "",
      };
    },
    methods: {
      validateInput() {
        console.log('PreguntaInput > this.questionText', this.questionText);
        
        this.$emit("update:value", this.questionText);
      },
    },
  };
  </script>
  