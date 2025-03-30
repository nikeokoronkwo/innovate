<template>
  <div class="flex min-h-lvh flex-col items-center justify-center align-middle">
    <span class="text-3xl font-bold">Redirecting...</span>
  </div>
</template>

<script setup lang="ts">
definePageMeta({
  middleware: "auth",
});

onMounted(() => navigateTo('/login'));
</script>
