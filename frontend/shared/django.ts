const config = useRuntimeConfig();

export const djangoUrl = config.djangoUrl;
export const djangoActive = config.djangoActive !== 0;

export const $django = $fetch.create({
  baseURL: djangoUrl,
  onRequest({ request, options, error }) {
    /** @todo: Handle error */
  },
  // async onResponseError({ response }) {
  //     if (response.status === 401) {
  //       await nuxtApp.runWithContext(() => navigateTo('/login'))
  //     }
  // }
});

export const useDjango = () => {
  return {
    active: djangoActive,
  };
};
