<template>
    <div class="mb-4">
        <label class="block mb-2 text-sm font-medium text-gray-700">
            Selecciona un archivo PDF:
        </label>
        <input type="file" accept="application/pdf" @change="handleFileUpload"
            class="block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 focus:outline-none" />
        <p v-if="fileName" class="text-sm text-green-600 mt-2">
            Archivo seleccionado: {{ fileName }}
        </p>
    </div>
</template>

<script>
export default {
    data() {
        return {
            fileName: null,
        };
    },
    methods: {
        handleFileUpload(event) {
            const file = event.target.files[0];
            this.fileName = file.name;
            this.$emit("file-selected", file);
        },
    },
};
</script>
