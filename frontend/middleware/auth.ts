export default defineNuxtRouteMiddleware((to, from) => {
  const { loggedIn, session, user, clear, fetch } = useUserSession();
});
