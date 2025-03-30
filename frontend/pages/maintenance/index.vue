<script setup lang="ts">
definePageMeta({
  layout: "dashboard",
});

const userData = useSampleData();

const maintenance = userData.maintenance;
</script>

<template>
  <div>
    <DashboardHeader title="Maintenance Requests" />

    <!-- Supplies Page -->
    <div>
      <div v-if="maintenance.length === 0">
        <!-- If empty, show something else -->
        <div
          class="my-auto flex flex-col items-center justify-center p-6 align-middle"
        >
          <span class="text-sm"
            >Maintenance Requests made can be found here</span
          >
        </div>
      </div>
      <div v-else>
        <!-- Search For Supplies -->

        <!-- Grid of Supplies -->

        <!-- Request Supplies -->
      </div>
    </div>

    <div class="fixed right-10 bottom-10 p-4">
      <Button
        rounded
        label="New Maintenance Request"
        asChild
        v-slot="slotProps"
      >
        <NuxtLink to="/maintenance/request" :class="slotProps.class"
          >New Maintenance Request</NuxtLink
        >
      </Button>
    </div>
  </div>
</template>
