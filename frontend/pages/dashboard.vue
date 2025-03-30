<script setup lang="ts">
definePageMeta({
  layout: "dashboard",
});

const u = useSampleData();
const user = u.user;

const speedDialItems = ref([
  {
    name: "Request New Item",
    icon: "mdi:file-plus",
    description: "Create a new file",
    action: () => console.log("New File"),
  },
  {
    name: "Report Feedback",
    icon: "mdi:upload",
    description: "Upload a file",
    action: () => console.log("Upload File"),
  },
]);

const tasks1 = ref([
  {
    id: 1,
    title: "Coca Cola",
    quantity: 2,
    description: "Tracking info A",
    status: "Pending",
  },
  {
    id: 2,
    title: "Task B",
    description: "Tracking info B",
    status: "Completed",
  },
]);

const tasks2 = ref([
  {
    id: 3,
    title: "Task X",
    detail: "Different tracking info X",
    status: "In Progress",
  },
  {
    id: 4,
    title: "Task Y",
    detail: "Different tracking info Y",
    status: "Pending",
  },
]);

const statusClasses = (status) => {
  return (
    {
      Pending: "bg-yellow-200 text-yellow-800",
      Completed: "bg-green-200 text-green-800",
      "In Progress": "bg-blue-200 text-blue-800",
    }[status] || "bg-gray-200 text-gray-800"
  );
};
</script>

<template>
  <!-- Dashboard Page -->
  <div>
    <DashboardHeader title="Dashboard" />

    <div class="flex min-h-lvh bg-gray-100 p-4">
      <aside class="w-1/4 rounded-2xl bg-white p-4 shadow-lg">
        <div class="flex flex-col items-center text-center">
          <Avatar
            :label="user.firstName[0]"
            class="mr-2"
            size="large"
            shape="circle"
          />
          <h2 class="text-lg font-semibold">
            {{ user.firstName + " " + user.lastName }}
          </h2>
          <p class="text-sm text-gray-500">{{ user.email }}</p>
        </div>
      </aside>
      <main class="min-h-xl flex-1 p-4">
        <Tabs value="0">
          <TabList>
            <Tab value="0">Supply Requests</Tab>
            <Tab value="1">Maintenance Requests</Tab>
          </TabList>
          <TabPanels>
            <TabPanel value="0">
              <div class="grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3">
                <Card
                  v-for="task in tasks1"
                  :key="task.id"
                  class="rounded-2xl shadow-lg"
                >
                  <template #title>{{ task.title }}</template>
                  <template #footer>
                    <Button
                      asChild
                      v-slot="slotProps"
                      severity="secondary"
                      rounded
                    >
                      <NuxtLink
                        :to="`/supplies/track/${task.id}`"
                        :class="slotProps.class"
                        >View More</NuxtLink
                      >
                    </Button>
                  </template>
                  <template #content>
                    <p class="text-sm text-gray-600">
                      x<span class="font-semibold">{{
                        task.quantity ?? 0
                      }}</span>
                    </p>
                    <span
                      :class="statusClasses(task.status)"
                      class="mt-2 inline-block rounded-full px-2 py-1 text-xs font-semibold"
                      >{{ task.status }}</span
                    >
                  </template>
                </Card>
              </div>
            </TabPanel>
            <TabPanel value="1">
              <div class="grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3">
                <Card
                  v-for="task in tasks2"
                  :key="task.id"
                  class="rounded-2xl shadow-lg"
                >
                  <template #title>{{ task.title }}</template>
                  <template #content>
                    <p class="text-sm text-gray-600">{{ task.detail }}</p>
                    <span
                      :class="statusClasses(task.status)"
                      class="mt-2 inline-block rounded-full px-2 py-1 text-xs font-semibold"
                      >{{ task.status }}</span
                    >
                  </template>
                </Card>
              </div>
            </TabPanel>
          </TabPanels>
        </Tabs>

        <!-- Dashboard Section 2 -->
      </main>
    </div>

    <!-- TODO: Quick Actions At Bottom -->
    <div class="fixed right-10 bottom-10">
      <SpeedDial :model="speedDialItems" direction="up" :transitionDelay="80">
        <!-- Main Button to Open/Close SpeedDial -->
        <template #button="{ toggleCallback }">
          <Button
            v-tooltip.left="'Quick Actions'"
            outlined
            class="rounded-full border p-2"
            @click="toggleCallback"
          >
            <Icon name="radix-icons:cross-2" class="text-lg" />
          </Button>
        </template>

        <!-- Individual Quick Action Buttons -->
        <template #item="{ item, toggleCallback }">
          <Button
            v-tooltip.left="item.description"
            outlined
            class="border-surface-200 dark:border-surface-700 flex items-center justify-center rounded-full border p-2"
            @click="
              item.action;
              toggleCallback;
            "
          >
            <Icon :name="item.icon" class="text-xl" />
          </Button>
        </template>
      </SpeedDial>
    </div>
  </div>
</template>
