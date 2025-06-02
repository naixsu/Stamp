<template>
    <!--
        TODO:
            - Handle color variables in different files
    -->
    <div
        v-if="modelValue"
        class="modal-overlay"
    >
        <div class="modal">
            <h3 class="modal-title">Add New Stamp Card</h3>

            <div class="form-group">
                <label for="title">Title</label>
                <div class="error-container">
                    <input
                        id="title"
                        v-model="form.title"
                        type="text"
                        placeholder="Enter a title"
                        :class="{
                            'invalid': errors.title
                        }"
                        @focus="errors.title = false"
                    />
                    <p
                        v-if="errors.title"
                        class="message"
                    >
                        Tite is required.
                    </p>
                </div>
            </div>

            <div class="form-group">
                <label for="stamps">Stamps Needed</label>
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

            <div class="modal-actions">
                <Button
                    label="Submit"
                    icon="check"
                    size="small"
                    color="success"
                    @click="handleSubmit"
                />
                <Button
                    label="Cancel"
                    icon="close"
                    size="small"
                    color="danger"
                    @click="handleCancel"
                />
            </div>
        </div>
    </div>
</template>

<script setup>
    import { reactive, ref, computed } from 'vue'
    import Button from '../generics/Button.vue'

    const props = defineProps({
        modelValue: Boolean,
    })

    const emit = defineEmits(['update:modelValue', 'submit'])

    // Data
    const errors = ref({
        title: false,
        stampsNeeded: false,
    })
    const form = reactive({
        title: '',
        stamps_needed: 1,
    })

    function handleSubmit() {
        // Validate errors
        const isEmpty = value =>
            value === null || value === undefined || value === '';

        if (form.stamps_needed < 1 || form.stamps_needed > 20) {
            errors.value.stampsNeeded = true;
        }

        if (isEmpty(form.title)) {
            errors.value.title = true;
        }

        if (Object.values(errors.value).some(error => error === true)) {
            return;
        }

        emit('submit', {
            ...form,
        })

        form.title = ''
        form.stamps_needed = 1
        emit('update:modelValue', false)
    }

    function handleCancel() {
        emit('update:modelValue', false)
    }
</script>

<style scoped>
    .modal-overlay {
        position: fixed;
        inset: 0;
        background: rgba(0, 0, 0, 0.6);
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 1000;
    }

    .modal {
        background: #2f2e41;
        padding: 2rem;
        border-radius: 10px;
        width: 100%;
        max-width: 350px;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
        color: white;
    }

    .modal-title {
        margin-bottom: 1.25rem;
        font-size: 1.25rem;
        font-weight: bold;
        text-align: center;
    }

    .form-group {
        margin-bottom: 1rem;
    }

    label {
        display: block;
        margin-bottom: 0.35rem;
        font-size: 0.9rem;
    }

    input {
        box-sizing: border-box;
        width: 100%;
        padding: 0.5rem 0.75rem;
        font-size: 0.95rem;
        border: 1px solid #444;
        border-radius: 6px;
        background: #1e1d2b;
        color: white;
    }

    input::placeholder {
        color: #888;
    }

    input.invalid {
        border-color: #ED2B42;
        box-shadow: 0 0 0 4px rgba(#ED2B42, .25);
    }

    .modal-actions {
        display: flex;
        justify-content: flex-end;
        gap: 0.5rem;
        margin-top: 1rem;
    }

    .error-container {
        display: flex;
        flex-direction: column;
    }

    .error-container .message {
        display: flex;
        align-items: center;
        color: #ED2B42;
        font-size: 12px;
        line-height: 1.5;
        letter-spacing: 0;
    }
</style>
