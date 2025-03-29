<template>
    <div class="flex flex-col items-center justify-center min-h-lvh space-y-4 py-auto mt-auto mb-auto align-middle">
        <div>Login</div>
        <div class="flex flex-col items-center justify-center">
            <Form v-slot="$form" :initialValues @submit="onFormSubmit" class="flex flex-col space-y-5" >
                <div class="flex flex-col gap-1">
                    <InputText name="email" type="text" placeholder="Email" fluid />
                    <Message v-if="$form.username?.invalid" severity="error" size="small" variant="simple">{{ $form.username.error?.message }}</Message>
                </div>
                <div class="flex flex-col gap-1">
                    <Password name="password" placeholder="Password" :feedback="false" toggleMask fluid />
                    <Message v-if="$form.email?.invalid" severity="error" size="small" variant="simple">{{ $form.email.error?.message }}</Message>
                </div>
                <Button type="submit" severity="secondary" label="Submit" />
            </Form>
        </div>
    </div>
</template>

<script setup lang="ts">
import type { FormSubmitEvent } from '@primevue/forms/form';

const initialValues = reactive<LoginDetails>({
    email: '',
    password: ''
});

const toast = useToast();

const resolver = ({ values }) => {
    const errors = {};

    if (!values.username) {
        errors.username = [{ message: 'Username is required.' }];
    }

    return {
        values, // (Optional) Used to pass current form values to submit event.
        errors
    };
};

const onFormSubmit = ({ valid, values }: FormSubmitEvent<LoginDetails>) => {
    if (valid) {
        toast.add({
            severity: 'success',
            summary: 'Form is submitted.',
            life: 3000
        });
        login(values)
    }
};

async function login(details: LoginDetails) {
    return await navigateTo('/dashboard');
}
</script>