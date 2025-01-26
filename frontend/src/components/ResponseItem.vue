<template>
    <li class="mb-2 p-4 border border-gray-300 rounded bg-gray-50 shadow-sm">
        <strong class="text-gray-700">Pregunta {{ key }}:</strong>
        <p class="text-gray-800 ml-4">{{ response.question }}</p>
        <strong class="text-gray-700 mt-2 block">Respuesta:</strong>
        <p class="text-gray-800 ml-4">{{ response.answer }}</p>
    </li>
</template>

<script>
export default {
    props: {
        response: {
            type: Object,
            required: true,
        },
        key: {
            type: [String, Number],
            required: true,
        },
    },
};
</script>

<style scoped>
/* Agrega estilos adicionales si es necesario */
</style>
