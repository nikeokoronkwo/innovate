<template>
  <div class="relative inline-block text-left">
    <button
      class="bg-space-cadet hover:bg-space-cadet rounded-lg px-4 py-2 text-white focus:outline-none"
      @click="isOpen = !isOpen"
    >
      <slot>Dropdown</slot>
    </button>
    <div
      v-show="isOpen"
      class="absolute left-0 z-10 mt-2 w-48 rounded-lg border border-gray-300 bg-white shadow-lg"
    >
      <NuxtLink
        v-for="item in props.items.filter(i => i.link)"
        :key="item.name"
        class="block px-4 py-2 text-gray-700 hover:bg-gray-100"
        to="item.route"
      >
        {{ item.name }}
      </NuxtLink>
      <button
        v-for="item in props.items.filter(i => !i.link)"
        :key="item.name"
        class="block px-4 py-2 text-gray-700 w-full hover:bg-gray-100"
        @click="item.action"
      >
        {{ item.name }}
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
const isOpen = ref(false);

const props = defineProps<{
  items: Array<
    | {
        name: string;
        action: () => void | Promise<void>;
        link: undefined;
      }
    | {
        name: string;
        route: string;
        link: true;
      }
  >;
}>();
</script>
