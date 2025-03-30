<template>
  <div class="flex flex-col items-center justify-center align-middle min-h-lvh">
    <span class="font-bold text-3xl">Redirecting...</span>
  </div>
</template>

<script setup lang="ts">
definePageMeta({
  middleware: 'auth'
});
</script>
