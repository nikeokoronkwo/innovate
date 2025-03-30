<template>
  <div
    class="py-auto mt-auto mb-auto flex min-h-lvh flex-col items-center justify-center space-y-4 align-middle"
  >
    <div>Login</div>
    <div class="flex flex-col items-center justify-center">
      <Form
        v-slot="$form"
        :initialValues
        :resolver="resolver"
        @submit="onFormSubmit"
        class="flex flex-col space-y-5"
      >
        <div class="flex flex-col gap-1">
          <InputText name="email" type="text" placeholder="Email" fluid />
          <Message
            v-if="$form.email?.invalid"
            severity="error"
            size="small"
            variant="simple"
            >{{ $form.email.error?.message }}</Message
          >
        </div>
        <div class="flex flex-col gap-1">
          <Password
            name="password"
            placeholder="Password"
            :feedback="false"
            toggleMask
            fluid
          />
          <Message
            v-if="$form.password?.invalid"
            severity="error"
            size="small"
            variant="simple"
            >{{ $form.password.error?.message }}</Message
          >
        </div>
        <Button type="submit" severity="secondary" label="Submit" />
      </Form>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { FormSubmitEvent } from "@primevue/forms/form";
import { zodResolver } from "@primevue/forms/resolvers/zod";
import { loginValidator, type LoginInformation } from "~/shared/user";

const initialValues = reactive<LoginInformation>({
  email: "",
  password: "",
});

const toast = useToast();

const resolver = ref(zodResolver(loginValidator));

const onFormSubmit = ({ valid, values }: FormSubmitEvent<LoginInformation>) => {
  if (valid) {
    login(values);
  }
};

async function login(details: LoginInformation) {
  // run request
  try {
    const user = await $fetch("/api/auth", {
      method: "POST",
      body: JSON.stringify(details),
    });

    if (user) {
      await refreshSession();
      return await navigateTo("/dashboard");
    }
  } catch (error) {
    console.error(error);
  }
}
</script>
