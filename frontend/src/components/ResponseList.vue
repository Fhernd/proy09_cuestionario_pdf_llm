<template>
    <div v-if="Object.keys(responses).length" class="mt-6">
        <ul>
            <ResponseItem v-for="(response, key) in responses" :itemKey="key" :response="response" />
        </ul>
    </div>
</template>

<script>
import ResponseItem from './ResponseItem.vue';

export default {
    components: {
        ResponseItem,
    },
    props: {
        responses: {
            type: Object,
            required: true,
        },
    },
};
</script>

<style scoped>
/* Agrega estilos personalizados aquí si es necesario */
</style>