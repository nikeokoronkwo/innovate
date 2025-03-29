<script setup lang="ts">
async function requestSupply(supplyRequest) {
  await navigateTo("/dashboard");
}

/** @todo Replace with items catalog from DB */
const supplies = ref([
  { name: "Coca Cola", category: "drink" },
  { name: "Sprite", category: "drink" },
]);

// form initial data
const initialValues = ref({
  item: "",
  quantity: undefined,
  message: "",
});
</script>

<template>
  <div class="flex min-h-lvh flex-col items-center justify-center space-y-5">
    <div class="text-2xl font-bold">Request Supplies</div>
    <div>
      <!-- Form Time -->
      <Form
        v-slot="$form"
        :initial-values="initialValues"
        class="flex flex-col items-center justify-center p-4"
      >
        <div class="space-y-3">
          <!-- Item Type Request (load when retrieving) -->
          <Select
            name="item.name"
            editable
            showClear
            :options="supplies"
            optionLabel="name"
            placeholder="Select an Item to Request"
          />
          <!-- IF Custom, type custom -->

          <!-- Quantity -->
          <div>
            <InputNumber name="quantity" placeholder="Quantity" fluid />
            <Message
              v-if="$form.amount?.invalid"
              severity="error"
              size="small"
              variant="simple"
              >{{ $form.amount.error?.message }}</Message
            >
          </div>
          <!-- Message -->
          <Textarea
            name="message"
            placeholder="Message (optional)"
            rows="5"
            cols="30"
          />
        </div>
        <div class="flex flex-row justify-center space-x-3">
          <div class="flex items-center gap-2">
            <Checkbox inputId="next" value="Request Another Item" />
            <label for="next">Request Another Item</label>
          </div>
          <Button type="submit">Submit Request</Button>
        </div>
      </Form>
    </div>
  </div>
</template>
