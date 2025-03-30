export default defineNuxtRouteMiddleware((to, from) => {
  const { loggedIn, session, user, clear, fetch } = useUserSession();

  if (loggedIn.value) {
    return navigateTo('/dashboard');
  } else {
    return navigateTo('/login')
  }
});
