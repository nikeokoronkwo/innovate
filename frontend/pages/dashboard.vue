<script setup lang="ts">
definePageMeta({
    layout: 'dashboard'
});

const u = useSampleData();
const user = u.user;

const speedDialItems = ref([{
    label: 'Request New Item',
    icon: 'ic:round-plus',
    command: () => {}
}, {
    label: 'Anonymous Feedback',
    icon: 'material-symbols:feedback-rounded',
}])
</script>

<template>
    <!-- Dashboard Page -->
    <div>
        <!-- Dashboard Header -->
        <div class="shadow flex flex-row justify-between p-4 rounded-sm text-xl">
            <!-- title -->
            <div>
                <span>Dashboard</span>
            </div>

            <!-- actions -->
            <div class="flex flex-row justify-between space-x-4">
                <NuxtLink to="/items">Supplies</NuxtLink>
                <NuxtLink to="/maintenance">Maintenance</NuxtLink>
                <NuxtLink to="/suggestions">Suggestions</NuxtLink>
            </div>
        </div>

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
        <div class="fixed bottom-10 right-10">
            <SpeedDial :model="speedDialItems" direction="up" :transitionDelay="80" >
                <template #button="{ toggleCallback }">
                    <Button v-tooltip="'Quick Actions'" outlined class="border rounded" @click="toggleCallback">
                        <Icon name="radix-icons:cross-2" />
                    </Button>
                </template>
                <template #item="{ item, toggleCallback }">
                    <Button :v-tooltip="item.name" outlined class="flex items-center justify-center py-2 border rounded border-surface-200 dark:border-surface-700 cursor-pointer"  @click="toggleCallback">
                        <Icon :name="item.icon" />
                    </Button>
                </template>
            </SpeedDial>
        </div>
    </div>
</template>