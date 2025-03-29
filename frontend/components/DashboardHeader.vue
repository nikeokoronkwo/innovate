<script setup lang="ts">
const props = defineProps({
  title: String,
});
</script>

<template>
  <!-- Dashboard Header -->
  <div class="flex flex-row justify-between rounded-sm p-4 text-xl shadow">
    <!-- title -->
    <div>
      <span>{{ props.title }}</span>
    </div>

    <!-- actions -->
    <div class="flex flex-row justify-between space-x-4">
      <NuxtLink to="/supplies">Supplies</NuxtLink>
      <NuxtLink to="/maintenance">Maintenance</NuxtLink>
      <NuxtLink to="/suggestions">Suggestions</NuxtLink>
    </div>
  </div>
</template>
