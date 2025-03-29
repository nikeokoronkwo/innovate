<script setup lang="ts">
definePageMeta({
  layout: "dashboard",
});

const sampleData = useSampleData();

const supplies = sampleData.supplies;
</script>

<template>
  <div>
    <DashboardHeader title="Supplies" />

    <!-- Supplies Page -->
    <div>
      <div v-if="supplies.length === 0">
        <!-- If empty, show something else -->
        <div
          class="my-auto flex flex-col items-center justify-center p-6 align-middle"
        >
          <span class="text-sm">There are no supplies here</span>
          <NuxtLink to="/supplies/request"> Request Supplies </NuxtLink>
        </div>
      </div>
      <div v-else>
        <!-- Search For Supplies -->

        <!-- Grid of Supplies -->

        <!-- Request Supplies -->
      </div>
    </div>
  </div>
</template>
