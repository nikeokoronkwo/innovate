<script setup lang="ts">
definePageMeta({
  layout: "dashboard",
});

const u = useSampleData();
const user = u.user;

const speedDialItems = ref([
  {
    label: "Request New Item",
    icon: "ic:round-plus",
    command: () => {},
  },
  {
    label: "Anonymous Feedback",
    icon: "material-symbols:feedback-rounded",
  },
]);
</script>

<template>
  <!-- Dashboard Page -->
  <div>
    <DashboardHeader title="Dashboard" />

    <!-- Dashboard Body -->
    <div class="py-4">
      <div class="flex flex-row justify-center text-2xl italic">
        Welcome {{ user.firstName }} {{ user.lastName[0].toUpperCase() }}.
      </div>
      <!-- User Info Section -->
      <section>
        <div></div>
        <div></div>
      </section>
      <section></section>
    </div>

    <!-- Dashboard Section 2 -->

    <!-- TODO: Quick Actions At Bottom -->
    <div class="fixed right-10 bottom-10">
      <SpeedDial :model="speedDialItems" direction="up" :transitionDelay="80">
        <template #button="{ toggleCallback }">
          <Button
            v-tooltip="'Quick Actions'"
            outlined
            class="rounded border"
            @click="toggleCallback"
          >
            <Icon name="radix-icons:cross-2" />
          </Button>
        </template>
        <template #item="{ item, toggleCallback }">
          <Button
            :v-tooltip="item.name"
            outlined
            class="border-surface-200 dark:border-surface-700 flex cursor-pointer items-center justify-center rounded border py-2"
            @click="toggleCallback"
          >
            <Icon :name="item.icon" />
          </Button>
        </template>
      </SpeedDial>
    </div>
  </div>
</template>
