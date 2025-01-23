<template>
    <div v-if="responses.length" class="mt-6">
        <h2 class="text-xl font-bold mb-4">Respuestas:</h2>
        <ul>
            <li v-for="(response, index) in responses" :key="index"
                class="mb-2 p-4 border border-gray-300 rounded bg-gray-50 shadow-sm">
                <strong class="text-gray-700">Pregunta {{ index + 1 }}:</strong>
                <p class="text-gray-800 ml-4">{{ response.question }}</p>
                <strong class="text-gray-700 mt-2 block">Respuesta:</strong>
                <p class="text-gray-800 ml-4">{{ response.answer }}</p>
            </li>
        </ul>
    </div>
</template>

<script>
export default {
    name: "ResponsesList",
    props: {
        responses: {
            type: Array,
            required: true,
        },
    },
};
</script>

<style scoped>
/* Agrega estilos personalizados aquí si es necesario */
</style>