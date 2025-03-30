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
]);
</script>

<template>
  <div class="flex flex-col">
    <!-- Top Navbar -->
    <header class="flex flex-row items-center justify-between p-4">
      <!-- Dashboard Title -->
      <!-- <div @click="navigateTo('/dashboard')" class="text-2xl">DN</div>
      <Dropper :items="dropDownItems">
        <div class="flex flex-row items-center">
          <Avatar
            :label="userData.firstName[0]"
            class="mr-2"
            size="large"
            shape="circle"
          />
          <div class="text-xl">{{ userData.email }}</div>
        </div>
      </Dropper> -->
      <Menubar :model="items" class="w-full">
        <template #start>
          <div @click="navigateTo('/dashboard')" class="text-2xl">DN</div>
        </template>
        <template #end>
          <Dropper :items="dropDownItems">
            <div class="flex flex-row items-center">
              <Avatar
                :label="userData.firstName[0]"
                class="mr-2"
                size="large"
                shape="circle"
              />
              <div class="text-xl">{{ userData.email }}</div>
            </div>
          </Dropper>
        </template>
      </Menubar>
      <!-- <div class="relative inline-block text-left" @mouseleave="isOpen = false">
        <button
          class="bg-space-cadet hover:bg-space-cadet z-10 rounded-lg px-4 py-2 text-white focus:outline-none"
          @click="isOpen = !isOpen"
          @mouseover="isOpen = true"
        >
          Dropdown
        </button>
        <div
          v-if="isOpen"
          class="relative left-0 -z-20 mt-2 w-full rounded-lg border border-gray-300 bg-white shadow-lg"
        >
          <a href="#" class="block px-4 py-2 text-gray-700 hover:bg-gray-100"
            >Item 1</a
          >
          <a href="#" class="block px-4 py-2 text-gray-700 hover:bg-gray-100"
            >Item 2</a
          >
          <a href="#" class="block px-4 py-2 text-gray-700 hover:bg-gray-100"
            >Item 3</a
          >
        </div>
      </div> -->
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

<style lang="css" scoped>
.p-menubar {
  border: none;
}
</style>
