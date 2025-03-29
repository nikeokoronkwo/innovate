<script setup lang="ts">
async function requestSupply(supplyRequest) {
    await navigateTo('/dashboard');
}

/** @todo Replace with items catalog from DB */
const items = ref([{ name: '' }])

// form initial data
const initialValues = ref({

})
</script>

<template>
    <div class="flex flex-col items-center justify-center min-h-lvh space-y-5">
        <div class="text-2xl font-bold ">Request Supplies</div>
        <div>
            <!-- Form Time -->
            <Form v-slot="$form" class="flex flex-col items-center justify-center p-4">
                <div class="space-y-3">
                    <!-- Item Type Request -->
                    <Select name="item" />
                    <!-- IF Custom, type custom -->


                    <!-- Quantity -->
                    <div>
                        <InputNumber name="quantity" inputId="integeronly" placeholder="Quantity" fluid />
                        <Message v-if="$form.amount?.invalid" severity="error" size="small" variant="simple">{{ $form.amount.error?.message }}</Message>
                    </div>
                    <!-- Message -->
                    <Textarea name="message" placeholder="Message (optional)" rows="5" cols="30" />
                </div>
                <Button></Button>
            </Form>
        </div>
    </div>
</template>