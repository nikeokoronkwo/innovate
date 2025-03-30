<script setup lang="ts">
// the current user data
const u = useSampleData();

const userData = u.user;
const isOpen = ref(false);
const { user, clear: clearSession } = useUserSession();

const dropDownItems = ref([
  {
    name: "Logout",
    action: async () => {
      console.log("weou");
      await clearSession();
      await navigateTo("/login");
    },
  },
]);

const selectedMenuOption = ref(null);

const items = ref([
  {
    label: "Home",
    icon: "pi pi-home",
    command: () => navigateTo("/dashboard"),
  },
  {
    label: "Supplies",
    // icon: "pi pi-search",
    // badge: 3, // TODO: API Reqs
    items: [
      {
        label: "View",
        icon: "pi pi-bolt",
        command: () => navigateTo("/supplies"),
      },
      {
        label: "Request",
        icon: "pi pi-server",
        command: () => navigateTo("/supplies/request"),
      },
    ],
  },
  {
    label: "Maintenance",
    items: [
      {
        label: "View",
        icon: "pi pi-bolt",
        command: () => navigateTo("/maintenance"),
      },
      {
        label: "Request",
        icon: "pi pi-server",
        command: () => navigateTo("/maintenance/request"),
      },
    ],
  },
  {
    label: "Support",
    command: () => navigateTo("/suggestions"),
  },
]);
</script>

<template>
  <div class="flex flex-col">
    <!-- Top Navbar -->
    <header
      class="bg-gray-100 p-4 text-gray-800 shadow-md dark:bg-gray-900 dark:text-white"
    >
      <Menubar :model="items" class="flex w-full items-center">
        <!-- Left: Dashboard Title -->
        <template #start>
          <div
            @click="navigateTo('/dashboard')"
            class="text-primary cursor-pointer text-2xl font-bold transition hover:opacity-80"
          >
            DN
          </div>
        </template>

        <!-- Right: User Avatar & Dropdown -->
        <template #end>
          <div class="flex items-center space-x-4">
            <div class="flex cursor-pointer items-center space-x-2">
              <Avatar
                :label="userData.firstName[0]"
                class="mr-2"
                size="large"
                shape="circle"
              />
              <span class="text-sm">{{ userData.email }}</span>
              <i class="pi pi-chevron-down text-sm"></i>
            </div>
          </div>
        </template>
      </Menubar>
    </header>

    <!-- TODO: Change this! -->
    <main class="min-h-lvh">
      <slot />
    </main>

    <!-- Bottom Navbar-->
    <footer
      class="bg-gray-100 p-6 text-gray-700 dark:bg-gray-900 dark:text-gray-300"
    >
      <div
        class="container mx-auto flex flex-col items-center justify-between md:flex-row"
      >
        <!-- Logo / Branding -->
        <div class="flex items-center space-x-2">
          <span class="text-primary text-2xl font-bold">DN</span>
        </div>

        <!-- Navigation Links -->
        <div class="flex flex-wrap justify-center space-x-6 text-sm">
          <a href="#" class="hover:text-primary transition">Help</a>
          <a href="#" class="hover:text-primary transition">Contact</a>
          <a href="#" class="hover:text-primary transition">Feedback</a>
          <a href="#" class="hover:text-primary transition">Privacy Policy</a>
          <a href="#" class="hover:text-primary transition">Terms of Service</a>
        </div>

        <!-- Social Media Icons -->
        <div class="flex space-x-4">
          <a href="#" class="hover:text-primary transition"
            ><i class="pi pi-facebook text-lg"></i
          ></a>
          <a href="#" class="hover:text-primary transition"
            ><i class="pi pi-twitter text-lg"></i
          ></a>
          <a href="#" class="hover:text-primary transition"
            ><i class="pi pi-instagram text-lg"></i
          ></a>
          <a href="#" class="hover:text-primary transition"
            ><i class="pi pi-linkedin text-lg"></i
          ></a>
        </div>
      </div>

      <!-- Copyright Section -->
      <div class="mt-4 text-center text-xs text-gray-500">
        &copy; {{ new Date().getFullYear() }} DN. All rights reserved.
      </div>
    </footer>
  </div>
</template>

<style lang="css" scoped>
.p-menubar {
  border: none;
}
</style>
