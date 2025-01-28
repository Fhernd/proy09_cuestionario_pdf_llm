<template>
    <li class="mb-2 p-4 border border-gray-300 rounded bg-gray-50 shadow-sm">
        <strong class="text-gray-700">Pregunta:</strong>
        <p class="text-gray-800 ml-4">{{ itemKey }}</p>
        <strong class="text-gray-700 mt-2 block">Respuesta:</strong>
        <p class="text-gray-800 ml-4">{{ response[itemKey] }}</p>
    </li>
</template>

<script>
export default {
    props: {
        response: {
            type: Object,
            required: true,
        },
        itemKey: {
            type: [String, Number],
            required: true,
        },
    },
};
</script>

<style scoped>
/* Agrega estilos adicionales si es necesario */
</style>
