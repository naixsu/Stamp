<template>
    <!--
        TODO:
            - Handle max char length for card titles
            - Make modal better
            - Add notes field
            - Add icon types for notes
            - Add char counter for notes
    -->
    <div
        class="modal-overlay"
        @click.self="emit('close')"
    >
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
                        :class="{
                            'invalid': errors.title || errors.duplicate
                        }"
                        @focus="
                            errors.title = false;
                            errors.duplicate = false;
                            "
                    />
                    <p
                        v-if="errors.title"
                        class="message"
                    >
                        Title is required.
                    </p>
                    <p
                        v-if="errors.duplicate"
                        class="message"
                    >
                        Duplicate title.
                    </p>
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
                        Enter a valid stamp count (1–20 only).
                    </p>
                </div>
            </div>

            <div class="form-group">
                <label for="notes">
                    Notes (optional)
                </label>

                <div class="error-container">
                    <textarea
                        v-model="form.notes"
                        placeholder="Extra info..."
                    />
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
        stampsNeeded: false,
        duplicate: false,
    })

    const form = reactive({
        title: '',
        stamps_needed: 1,
        notes: '',
    })

    function handleSubmit() {
        // Validate errors
        const isEmpty = value =>
            value === null || value === undefined || value === '';

        // Errors
        // Stamp # error
        if (form.stamps_needed < 1 || form.stamps_needed > 20) {
            errors.value.stampsNeeded = true;
        }

        // No title
        if (isEmpty(form.title)) {
            errors.value.title = true;
        }

        // Duplicate title
        const normalizedTitle = form.title.toLowerCase();
        const isDuplicate = props.existingCards.some(card=>
            card.title.toLowerCase() === normalizedTitle
        );

        if (isDuplicate) {
            errors.value.duplicate = true;
        }

        if (Object.values(errors.value).some(error => error === true)) {
            return;
        }

        emit('submit', {
            ...form,
        })

        form.title = ''
        form.stamps_needed = 1
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
        margin-bottom: 1.25rem;
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

    textarea {
        resize: none;
        height: 100px;
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

    input.invalid {
        border-color: var(--color-danger);
        background-color: var(--color-danger-focus);
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
        margin-top: 0.3rem;
        padding-left: 0.25rem;
    }
</style>
