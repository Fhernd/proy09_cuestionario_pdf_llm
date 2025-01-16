<template>
    <div class="mb-4">
        <label class="block mb-2 text-sm font-medium text-gray-700">
            
        </label>
        <div class="flex items-center">
            <input type="file" accept="application/pdf" @change="handleFileUpload" ref="fileInput" class="hidden" />
            <button @click="triggerFileInput"
                class="bg-blue-500 text-white px-4 py-2 rounded-lg cursor-pointer hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-400 focus:border-transparent w-full">
                Seleccionar archivo
            </button>
            <p v-if="fileName" class="text-sm text-green-600 mt-2 ml-4">
                Archivo seleccionado: {{ fileName }}
            </p>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            fileName: ''
        };
    },
    methods: {
        handleFileUpload(event) {
            const file = event.target.files[0];
            if (file) {
                this.fileName = file.name;
                this.$emit('file-selected', file);
            }
        },
        triggerFileInput() {
            this.$refs.fileInput.click();
        }
    }
};
</script>