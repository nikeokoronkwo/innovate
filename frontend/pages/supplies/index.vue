<script setup lang="ts">
definePageMeta({
  layout: "dashboard",
});

// Fetch sample data (assuming it contains ordered supplies)
const sampleData = useSampleData();
const supplies = ref(sampleData.supplies);
</script>

<template>
  <div>
    <DashboardHeader title="Supplies" />

    <div class="p-6">
      <div
        v-if="supplies.length === 0"
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
          class="mt-4 rounded-md bg-space-cadet px-4 py-2 text-white transition hover:bg-space-cadet"
        >
          Request Supplies
        </NuxtLink>
      </div>

      <div v-else>
        <!-- Supplies Data View -->
        <DataView :value="supplies" layout="grid">
          <template #grid="slotProps">
            <div
              class="rounded-md border bg-white p-4 shadow-md dark:bg-gray-800"
            >
              <div class="flex items-center justify-between">
                <h3 class="text-lg font-semibold text-gray-800 dark:text-white">
                  {{ slotProps.data.name }}
                </h3>
                <span
                  :class="{
                    'text-green-500': slotProps.data.remaining > 10,
                    'text-yellow-500':
                      slotProps.data.remaining <= 10 &&
                      slotProps.data.remaining > 3,
                    'text-red-500': slotProps.data.remaining <= 3,
                  }"
                >
                  {{ slotProps.data.remaining }} left
                </span>
              </div>
              <p class="mt-2 text-gray-600 dark:text-gray-300">
                {{ slotProps.data.description }}
              </p>
              <div class="mt-4 flex items-center justify-between">
                <span class="text-sm text-gray-500 dark:text-gray-400">
                  Ordered on:
                  {{ new Date(slotProps.data.orderedAt).toLocaleDateString() }}
                </span>
                <NuxtLink
                  to="/supplies/request"
                  class="text-sm text-blue-500 hover:underline"
                >
                  Reorder
                </NuxtLink>
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
