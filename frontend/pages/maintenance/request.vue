<template>
  <div class="p-4">
    <Card>
      <template #title>Submit Maintenance Request</template>
      <template #content>
        <Form
          v-slot="$form"
          :initial-values="initialValues"
          :resolver="resolver"
          class="flex flex-col gap-5 p-4"
        >
          <FloatLabel>
            <label for="title" class="block text-sm font-medium">Title</label>
            <InputText id="title" name="title" class="w-full" />
          </FloatLabel>
          <Message
            v-if="$form.title?.invalid"
            severity="error"
            size="small"
            variant="simple"
            >{{ $form.title.error?.message }}</Message
          >

          <!-- TODO: Kind of item for maintenance -->

          <!-- <FloatLabel>
            <label for="image" class="block text-sm font-medium"
              >Upload Images (if applicable)</label
            >
            <FileUpload
              id="image"
              mode="basic"
              accept="image/*"
              :auto="true"
              @select="onImageSelect"
            />
          </FloatLabel> -->

          <div>
            <label for="editor" class="block py-2 text-sm font-medium"
              >Description</label
            >
            <Editor
              id="editor"
              name="description"
              class="w-full"
              editorStyle="height: 220px"
            />
          </div>
          <Message
            v-if="$form.description?.invalid"
            severity="error"
            size="small"
            variant="simple"
            >{{ $form.description.error?.message }}</Message
          >

          <Button
            type="submit"
            label="Submit Maintenance Request"
            class="mt-4"
          />
        </Form>
      </template>
    </Card>
  </div>
</template>

<script setup lang="ts">
import type { FormSubmitEvent } from "@primevue/forms/form";
import { zodResolver } from "@primevue/forms/resolvers/zod";

definePageMeta({
  layout: "dashboard",
});

const initialValues = ref({
  title: "",
  // images: null, // TODO: Images
  description: "",
});

const resolver = ref(zodResolver(maintenanceReqValidation));

// const onImageSelect = (event) => {
//   formData.value.image = event.files[0];
// };

const onSubmit = ({ valid, values }: FormSubmitEvent<MaintenanceRequest>) => {
  // submit
  if (valid) {
  }
};
</script>
