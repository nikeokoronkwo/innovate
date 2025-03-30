<script setup lang="ts">
definePageMeta({
  layout: "dashboard",
});

// Mock Inventory Data
const inventory = ref([
  {
    id: "inv-001",
    name: "Printer Paper",
    category: "office",
    quantity: 50,
  },
  {
    id: "inv-002",
    name: "Toner Cartridge",
    category: "office",
    quantity: 5,
  },
  {
    id: "inv-003",
    name: "Whiteboard Markers",
    category: "office",
    quantity: 20,
  },
]);

// Mock Supply Requests Data
const supplyRequests = ref([
  {
    id: "req-001",
    userId: "user-123",
    itemId: "inv-001",
    amount: 10,
    dateRequested: "2024-03-20",
    delay: false,
    messages: ["Request approved", "Expected delivery in 2 days"],
  },
  {
    id: "req-002",
    userId: "user-123",
    itemId: "inv-002",
    amount: 2,
    dateRequested: "2024-03-18",
    delay: true,
    messages: ["Supply delayed due to stock issues"],
  },
]);

// Combine supply requests with inventory details
const userSupplies = computed(() => {
  return supplyRequests.value.map((request) => {
    const item = inventory.value.find((inv) => inv.id === request.itemId);
    return {
      ...request,
      name: item?.name || "Unknown Item",
      category: item?.category || "other",
      remaining: item?.quantity || 0,
    };
  });
});
</script>

<template>
  <div>
    <DashboardHeader title="Supplies" />

    <div class="p-6">
      <div
        v-if="userSupplies.length === 0"
        class="flex flex-col items-center text-center"
      >
        <!-- Empty State UI -->
        <img alt="No Supplies" class="mb-4 h-32 w-32" />
        <h2 class="text-lg font-semibold text-gray-600 dark:text-gray-300">
          You do not have any supplies left
        </h2>
        <p class="text-gray-500 dark:text-gray-400">
          Request new supplies to keep your inventory stocked.
        </p>
        <NuxtLink
          to="/supplies/request"
          class="mt-4 rounded-md bg-blue-600 px-4 py-2 text-white transition hover:bg-blue-700"
        >
          Request Supplies
        </NuxtLink>
      </div>

      <div v-else>
        <!-- Supplies Data View -->
        <DataView :value="userSupplies" layout="grid">
          <template #grid="slotProps">
            <div class="grid grid-cols-3 gap-4">
              <div
                v-for="(item, index) in slotProps.items"
                :key="index"
                class="rounded-md border bg-white p-4 shadow-md dark:bg-gray-800"
              >
                <div class="flex items-center justify-between">
                  <h3
                    class="text-lg font-semibold text-gray-800 dark:text-white"
                  >
                    {{ item.name }}
                  </h3>
                  <span
                    :class="{
                      'text-green-500': item.remaining > 10,
                      'text-yellow-500':
                        item.remaining <= 10 && item.remaining > 3,
                      'text-red-500': item.remaining <= 3,
                    }"
                  >
                    {{ item.remaining }} left
                  </span>
                </div>
                <p class="mt-2 text-gray-600 dark:text-gray-300">
                  Category: {{ item.category }}
                </p>
                <p class="text-sm text-gray-500 dark:text-gray-400">
                  Requested:
                  {{ new Date(item.dateRequested).toLocaleDateString() }}
                </p>
                <p class="mt-2 text-sm text-red-500" v-if="item.delay">
                  ⚠ Supply delayed
                </p>
                <ul
                  v-if="item.messages.length > 0"
                  class="mt-2 text-xs text-gray-500"
                >
                  <li v-for="(msg, index) in item.messages" :key="index">
                    • {{ msg }}
                  </li>
                </ul>
                <div class="mt-4 flex items-center justify-between">
                  <NuxtLink
                    to="/supplies/request"
                    class="text-sm text-blue-500 hover:underline"
                  >
                    Reorder
                  </NuxtLink>
                </div>
              </div>
            </div>
          </template>
        </DataView>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* Tailwind Utility Classes Used */
</style>
