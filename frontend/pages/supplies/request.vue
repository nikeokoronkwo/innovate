<script setup lang="ts">

const router = useRouter();
const toast = useToast();

// Mock Inventory Data (Fetched from DB in real case)
const inventory = ref([
  { id: "inv-001", name: "Printer Paper", category: "office", quantity: 50 },
  { id: "inv-002", name: "Toner Cartridge", category: "office", quantity: 5 },
  { id: "inv-003", name: "Whiteboard Markers", category: "office", quantity: 20 },
]);

// Stepper State
const step = ref(1);

// Cart (User-selected items)
const cart = ref<Record<string, number>>({});
const extraInfo= ref<string | undefined>(undefined);

// Add item to cart
const addItem = (id: string) => {
  if (!cart.value[id]) cart.value[id] = 0;
  cart.value[id]++;
};

// Remove item from cart
const removeItem = (id: string) => {
  if (cart.value[id]) cart.value[id]--;
  if (cart.value[id] === 0) delete cart.value[id]; // Remove item if quantity is 0
};

// Get selected items
const selectedItems = computed(() => {
  return inventory.value.filter((item) => cart.value[item.id]);
});

// Get total quantity selected
const totalQuantity = computed(() => {
  return Object.values(cart.value).reduce((sum, qty) => sum + qty, 0);
});

// Submit Request
const submitRequest = () => {
  toast.add({ severity: "success", summary: "Request Submitted", detail: "Your supplies request has been sent!", life: 3000 });
  cart.value = {}; // Clear cart
  step.value = 1; // Reset stepper
  return navigateTo('/dashboard')// Redirect back
};
</script>

<template>
  <div>
    <DashboardHeader title="Request Supplies" />

    <!-- Stepper -->
    <Stepper :value="1" linear class="my-4">
      <StepList>
        <Step :value="1">Select Items</Step>
        <Step :value="2">Checkout</Step>
      </StepList>
      <StepPanels>
        <StepPanel v-slot="{ activateCallback }" :value="1">
          <div class="p-4">
            <DataView :value="inventory" layout="grid">
              <template #grid="slotProps">
                <div 
                    v-for="(item, index) in slotProps.items"
                    :key="index"
                    class="p-4 border rounded-md shadow-md bg-white dark:bg-gray-800"
                >
                  <h3 class="text-lg font-semibold text-gray-800 dark:text-white">
                    {{ item.name }}
                  </h3>
                  <p class="text-gray-600 dark:text-gray-300">
                    Category: {{ item.category }}
                  </p>
                  <div class="flex items-center mt-4">
                    <button @click="removeItem(item.id)" class="px-3 py-1 bg-gray-300 dark:bg-gray-700 rounded-md">−</button>
                    <span class="mx-3 text-lg">{{ cart[item.id] || 0 }}</span>
                    <button @click="addItem(item.id)" class="px-3 py-1 bg-blue-500 text-white rounded-md">+</button>
                  </div>
                </div>
              </template>
            </DataView>
            <div class="flex justify-end mt-6">
              <Button @click="activateCallback(2)" class="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 transition" :disabled="totalQuantity === 0">
                Continue to Checkout
              </Button>
            </div>
          </div>
      </StepPanel>

      <StepPanel v-slot="{ activateCallback }" :value="2">
          <div class="p-6">
            <h2 class="text-xl font-semibold mb-4">Order Summary</h2>
            <div v-if="selectedItems.length > 0">
              <div v-for="item in selectedItems" :key="item.id" class="p-4 border rounded-md bg-white dark:bg-gray-800 mb-2">
                <h3 class="text-lg">{{ item.name }}</h3>
                <p>Quantity: {{ cart[item.id] }}</p>
              </div>
              <p class="text-lg font-semibold mt-4">Total Items: {{ totalQuantity }}</p>
              <div class="py-3">
                <Textarea
                    v-model="extraInfo"
                    placeholder="Add any additional info here (optional)"
                    rows="5"
                    cols="30"
                    fluid
                />
              </div>
              
              <div class="flex justify-between mt-6">
                <Button @click="activateCallback(1)" severity="secondary">
                  Back
                </Button>
                <Button @click="submitRequest">
                  Submit Request
                </Button>
              </div>
            </div>
            <div v-else>
              <p class="text-gray-600">No items selected. Go back and add some supplies.</p>
            </div>
          </div>
      </StepPanel>
      </StepPanels>
    </Stepper>
  </div>
</template>
