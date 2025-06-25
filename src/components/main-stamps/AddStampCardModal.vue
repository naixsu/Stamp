<template>
    <!--
        TODO:
            - Add icon types for notes
    -->
    <div class="modal-overlay">
        <div class="modal">
            <h3 class="modal-title">
                Add New Stamp Card
            </h3>

            <div class="form-group">
                <label for="title">
                    Title
                </label>
                <div class="error-container">
                    <input
                        id="title"
                        v-model.trim="form.title"
                        type="text"
                        placeholder="Enter title"
                        maxlength="50"
                        :class="{
                            'invalid':
                                errors.title ||
                                errors.duplicate ||
                                errors.titleExceed
                        }"
                        @focus="
                            errors.title = false;
                            errors.titleExceed = false;
                            errors.duplicate = false;
                        "
                    />
                    <div class="inline-error">
                        <p
                            v-if="errors.title"
                            class="message"
                        >
                            Title is required.
                        </p>
                        <p
                            v-else-if="errors.duplicate"
                            class="message"
                        >
                            Duplicate title.
                        </p>
                        <p
                            v-else-if="errors.titleExceed"
                            class="message"
                        >
                            Title is too long.
                        </p>
                        <p class="char-counter">
                            {{ form.title.length }}/{{ maxTitleLength }}
                        </p>
                    </div>
                </div>
            </div>

            <div class="form-group">
                <label for="stamps">
                    Stamps Needed
                </label>
                <div class="error-container">
                    <input
                        id="stamps"
                        v-model.number="form.stamps_needed"
                        type="number"
                        min="1"
                        max="20"
                        placeholder="Enter number of stamps"
                        :class="{
                            'invalid': errors.stampsNeeded
                        }"
                        @focus="errors.stampsNeeded = false"
                    />
                    <p
                        v-if="errors.stampsNeeded"
                        class="message"
                    >
                        Enter a valid stamp count (1-{{ maxStampsLength }}) only.
                    </p>
                </div>
            </div>

            <div class="form-group">
                <label for="notes">
                    Notes (optional)
                </label>

                <div class="error-container">
                    <textarea
                        id="notes"
                        v-model="form.notes"
                        placeholder="Extra info..."
                        :class="{
                            'invalid': errors.notesExceed
                        }"
                        @focus="errors.notesExceed = false"
                    />
                    <div class="inline-error">
                        <p
                            v-if="errors.notesExceed"
                            class="message"
                        >
                            Notes too long.
                        </p>
                        <p class="char-counter">
                            {{ form.notes.length }}/{{ maxNotesLength }}
                        </p>
                    </div>
                </div>
            </div>

            <div class="modal-actions">
                <Button
                    label="Submit"
                    icon="check"
                    size="medium"
                    color="primary"
                    @click="handleSubmit"
                />
                <Button
                    label="Cancel"
                    icon="close"
                    size="medium"
                    color="danger"
                    @click="handleCancel"
                />
            </div>
        </div>
    </div>
</template>

<script setup>
    import { reactive, ref } from 'vue'
    import Button from '../generics/Button.vue'

    const props = defineProps({
        existingCards: {
            type: Array,
            default: () => [],
        }
    })

    const emit = defineEmits(['close', 'submit'])

    // Data
    const errors = ref({
        title: false,
        titleExceed: false,
        stampsNeeded: false,
        duplicate: false,
        notesExceed: false,
    })

    const form = reactive({
        title: '',
        stamps_needed: 1,
        notes: '',
    })

    const maxTitleLength = ref(20);
    const maxStampsLength = ref(20);
    const maxNotesLength = ref(500);

    function handleSubmit() {
        const isEmpty = value => value === null || value === undefined || value === '';

        if (form.stamps_needed < 1 || form.stamps_needed > maxStampsLength.value) {
            errors.value.stampsNeeded = true;
        }

        if (form.title.length > maxTitleLength.value) {
            errors.value.titleExceed = true;
        }

        if (isEmpty(form.title)) {
            errors.value.title = true;
        }

        const normalizedTitle = form.title.toLowerCase();
        const isDuplicate = props.existingCards.some(card =>
            card.title.toLowerCase() === normalizedTitle
        );

        if (isDuplicate) {
            errors.value.duplicate = true;
        }

        if (form.notes.length > maxNotesLength.value) {
            errors.value.notesExceed = true;
        }

        if (Object.values(errors.value).some(error => error === true)) {
            return;
        }

        emit('submit', { ...form })

        form.title = ''
        form.stamps_needed = 1
        form.notes = ''
        emit('close')
    }

    function handleCancel() {
        emit('close')
    }
</script>

<style scoped>
    .modal-overlay {
        position: fixed;
        inset: 0;
        background: rgba(27, 45, 72, 0.5);
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 1000;
    }

    .modal {
        background-color: var(--color-modal-bg);
        padding: 2rem;
        border-radius: 1rem;
        width: 100%;
        max-width: 420px;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);
        font-family: 'Inter', sans-serif;
        color: #1b2d48;
    }

    .modal-title {
        margin-bottom: 1.5rem;
        font-size: 1.3rem;
        font-weight: 600;
        text-align: center;
    }

    .form-group {
        margin-bottom: 0.7rem;
    }

    label {
        display: block;
        margin-bottom: 0.4rem;
        font-size: 0.95rem;
        font-weight: 500;
        color: var(--color-text);
        font-size: 1rem;
    }

    input,
    textarea {
        border: 1px solid var(--color-wrapper-shadow);
        border-radius: 8px;
        padding: 0.6rem 0.8rem;
        font-family: inherit;
        transition: border 0.2s;
        background-color: var(--color-white-text);
        color: var(--color-text);
    }

    input::placeholder,
    textarea::placeholder {
        color: var(--color-text);
    }

    input:focus,
    textarea:focus {
        outline: none;
        border-color: var(--color-icon-border);
        background-color: var(--color-input-focus);
    }

    input.invalid,
    textarea.invalid {
        border-color: var(--color-danger);
        background-color: var(--color-danger-focus);
    }

    textarea {
        resize: none;
        height: 100px;
    }

    textarea::-webkit-scrollbar {
        width: 6px;
    }

    textarea::-webkit-scrollbar-track {
        background-color: var(--color-hover);
        border-radius: 3px;
        border-top-right-radius: 8px;
        border-bottom-right-radius: 8px;
    }

    textarea::-webkit-scrollbar-thumb {
        background-color: var(--color-text);
        border-radius: 3px;
    }

    .modal-actions {
        display: flex;
        justify-content: flex-end;
        gap: 0.75rem;
        margin-top: 1.5rem;
    }

    .error-container {
        display: flex;
        flex-direction: column;
    }

    .message {
        color: var(--color-danger);
        font-size: 0.8rem;
        margin-top: 0.25rem;
    }

    .char-counter {
        font-size: 0.8rem;
        margin-top: 0.25rem;
        margin-left: auto;
        color: var(--color-text);
    }

    .inline-error {
        display: flex;
        align-items: center;
        min-height: 1.2rem;
    }
</style>
