<template>
    <div class="flex flex-col">
        <!-- Top Navbar -->
        <header class="flex flex-row justify-between p-4">
            <!-- Dashboard Title -->
            <div></div>
            <div>
                <div></div>
                <div>{{ userData.email }}</div>
            </div>
        </header>

        <main>
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
const userData = {
    firstName: 'Lady',
    lastName: 'Gaga',
    email: 'ladygaga@dn.com'
};
</script>