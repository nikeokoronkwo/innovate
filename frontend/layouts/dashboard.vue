<template>
  <div class="flex flex-col">
    <!-- Top Navbar -->
    <header class="flex flex-row justify-between p-4">
      <!-- Dashboard Title -->
      <div></div>
      <div class="flex flex-row items-center">
        <Avatar :label="userData.firstName[0]" class="mr-2" size="large" shape="circle" />
        <div class="text-xl">{{ userData.email }}</div>
      </div>
    </header>

    <!-- TODO: Change this! -->
    <main class="min-h-lvh">
      <slot />
    </main>

    <!-- Bottom Navbar-->
    <footer>
      <!-- Footer -->
      <div>
        <div>
          <span>DN</span>
        </div>
        <div class="grid grid-cols-3 grid-rows-3 gap-2 p-4 text-sm">
          <div>Help</div>
          <div>Contact</div>
          <div>Feedback</div>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup lang="ts">
// the current user data
const u = useSampleData();

const userData = u.user;
</script>
