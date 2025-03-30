<script setup lang="ts">
import { feedbackTags } from "~/shared/tags";

definePageMeta({
  layout: "dashboard",
});

const { feedback } = useSampleData();

// The kinds of tags available
const tags = ref(feedbackTags);

const initialValues = ref({
  tags: [],
  content: "",
});

// on form submit
const onSubmit = ({ valid, values }) => {
  // submit
};
</script>

<template>
  <div>
    <DashboardHeader title="Feedback" />

    <div
      class="flex min-h-full flex-col items-center justify-center space-y-3 p-4"
    >
      <div class="text-2xl font-bold">Submit Feedback</div>
      <Form
        v-slot="$form"
        :initial-values="initialValues"
        class="flex flex-col items-center justify-center p-4"
      >
        <!-- Feedback Kind: Tags -->
        <div class="flex flex-col space-y-2.5">
          <!-- TODO: Tooltip info -->
          <MultiSelect
            name="tags"
            :options="tags"
            showClear
            filter
            optionLabel="name"
            :maxSelectedLabels="3"
            placeholder="Select Feedback Tag(s)"
            fluid
            class="w-full min-w-xl"
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
          <div class="flex w-full flex-col justify-start py-2">
            <div class="text-xl font-semibold">Feedback Content</div>
            <div class="text-sm">Enter your desired feedback here</div>
          </div>
          <div class="flex flex-col gap-1">
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
        </div>

        <!-- Submit feedback -->
        <Button type="submit" severity="secondary" label="Submit Feedback" />

        <DevOnly>
          <Fieldset legend="Form States" class="h-80 overflow-auto p-5">
            <pre class="whitespace-pre-wrap">{{ $form }}</pre>
          </Fieldset>
        </DevOnly>
      </Form>
    </div>
  </div>
</template>
