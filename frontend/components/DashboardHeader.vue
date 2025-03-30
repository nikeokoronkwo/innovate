<script setup lang="ts">
const props = defineProps({
  title: String,
});
</script>

<template>
  <!-- Dashboard Header -->
  <div
    class="bg-space-cadet flex flex-row justify-between p-4 text-xl text-white shadow"
  >
    <!-- title -->
    <div>
      <span class="font-bold">{{ props.title }}</span>
    </div>
  </div>
</template>
