<script setup lang="ts">
definePageMeta({
  layout: "dashboard",
});

import type { FormSubmitEvent } from "@primevue/forms/form";
import { $django, djangoActive, djangoUrl } from "~/shared/django";
import { feedbackTags } from "~/shared/tags";

// The kinds of tags available
const tags = ref(feedbackTags);

const initialValues = ref({
  tags: [],
  content: "",
});

// on form submit
const onSubmit = async ({ valid, values }: FormSubmitEvent) => {
  // submit
  if (valid) {
    console.log(djangoUrl, djangoActive);
    // make request
    const resp = await $django("/api/feedback/", {
      method: "POST",
      body: values,
    });

    console.log(resp);
  }
};
</script>

<template>
  <div>
    <div class="p-4">
      <Card>
        <template #title> Submit Feedback </template>
        <template #content>
          <Form
            v-slot="$form"
            :initial-values="initialValues"
            class="flex flex-col items-center justify-start gap-4 p-4"
            @submit="onSubmit"
          >
            <!-- Feedback Kind: Tags -->
            <div>
              <label for="tags" class="block text-lg font-semibold">Tags</label>
              <span class="block text-sm text-gray-500"
                >Select or add custom tags</span
              >
              <MultiSelect
                id="tags"
                name="tags"
                :options="tags"
                showClear
                filter
                optionLabel="name"
                :maxSelectedLabels="3"
                placeholder="Select Feedback Tag(s)"
                fluid
                class="min-w-xl py-2"
              />
              <div class="space-x-2 py-3">
                <Tag
                  v-for="tag in $form.tags?.value ?? []"
                  :key="tag"
                  rounded
                  :value="tag.name"
                  class="rounded-lg"
                />
              </div>
            </div>

            <!-- Feedback Content -->
            <div class="py-2">
              <label for="editor" class="block text-lg font-semibold"
                >Feedback Content</label
              >
              <span class="block text-sm text-gray-500"
                >Enter your desired feedback here</span
              >
              <Editor
                name="content"
                editorStyle="height: 320px"
                id="fb_content"
              />
              <Message
                v-if="$form.content?.invalid"
                severity="error"
                size="small"
                variant="simple"
                >{{ $form.content.error?.message }}</Message
              >
            </div>

            <!-- Submit feedback -->
            <Button
              type="submit"
              severity="secondary"
              label="Submit Feedback"
            />
          </Form>
        </template>
      </Card>
    </div>
  </div>
</template>
