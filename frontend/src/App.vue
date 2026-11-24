<script setup lang="ts">
import { onMounted, ref } from "vue";

interface Note {
    id: number;
    title: string;
    content: string;
    is_done: boolean;
    created_at: string;
}

const notes = ref<Note[]>([]);
const loading = ref(true);
const error = ref("");

onMounted(async () => {
    try {
        const response = await fetch("http://127.0.0.1:8000/api/notes/");

        if (!response.ok) {
            throw new Error(`Помилка сервера: ${response.status}`);
        }

        const data: { notes: Note[] } = await response.json();
        notes.value = data.notes;
    } catch (e) {
        error.value =
            e instanceof Error ? e.message : "Не вдалося завантажити нотатки";
    } finally {
        loading.value = false;
    }
});
</script>

<template>
    <main class="main">
        <h1>Нотатки</h1>

        <p v-if="loading">Завантаження...</p>
        <p v-else-if="error">{{ error }}</p>

        <ul v-else class="notes-grid">
            <li v-for="note in notes" :key="note.id" class="note-card">
                <strong>{{ note.title }}</strong>
                <p>{{ note.content }}</p>
                <span>{{ note.is_done ? "Виконано" : "Не виконано" }}</span>
            </li>
        </ul>
    </main>
</template>

<style scoped>
.main {
}

.notes-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
    gap: 12px;
    padding: 0;
    list-style: none;
}

.note-card {
    border: 1px solid #d1d5db;
    border-radius: 8px;
    padding: 12px;
}
</style>
