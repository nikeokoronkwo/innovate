import tailwindcss from "@tailwindcss/vite";
import Nora from "@primeuix/themes/nora";

export default defineNuxtConfig({
  compatibilityDate: "2024-11-01",
  devtools: { enabled: true },

  css: ["~/assets/css/main.css"],

  modules: [
    "@nuxt/icon",
    "@nuxt/test-utils",
    "@nuxt/eslint",
    "@nuxt/fonts",
    "@nuxt/image",
    "@primevue/nuxt-module",
    "nuxt-auth-utils",
  ],

  vite: {
    plugins: [tailwindcss()],
  },

  primevue: {
    options: {
      theme: {
        preset: Nora,
      },
    },
  },

  runtimeConfig: {
    public: {
      djangoUrl: "",
      djangoActive: 0,
    },
  },
});
