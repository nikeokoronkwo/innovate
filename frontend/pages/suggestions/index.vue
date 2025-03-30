<script setup lang="ts">
import { feedbackTags } from "~/shared/tags";

definePageMeta({
  layout: "dashboard",
});

// The kinds of tags available
const tags = ref(feedbackTags);

const initialValues = ref({
  tags: [],
  content: "",
});

// on form submit
const onSubmit = ({ valid, values }) => {
  // submit
  if (valid) {
    // make request
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
                class="min-w-xl"
              />
              <div class="space-x-2">
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

            <DevOnly>
              <Fieldset legend="Form States" class="h-80 overflow-auto p-5">
                <pre class="whitespace-pre-wrap">{{ $form }}</pre>
              </Fieldset>
            </DevOnly>
          </Form>
        </template>
      </Card>
    </div>
  </div>
</template>
