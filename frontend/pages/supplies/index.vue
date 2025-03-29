<script setup lang="ts">
definePageMeta({
    layout: 'dashboard'
})

const sampleData = useSampleData();

const supplies = sampleData.supplies;
</script>

<template>
    <div>
        <DashboardHeader title="Supplies" />

        <!-- Supplies Page -->
        <div>
            <div v-if="supplies.length === 0">
                <!-- If empty, show something else -->
                <div class="flex flex-col items-center justify-center align-middle my-auto p-6">
                    <span class="text-sm">There are no supplies here</span>
                    <NuxtLink to="/supplies/request">
                        Request Supplies
                    </NuxtLink>
                </div>
            </div>
            <div v-else>
                <!-- Search For Supplies -->

                <!-- Grid of Supplies -->


                <!-- Request Supplies -->
            </div>
        </div>
    </div>
</template>