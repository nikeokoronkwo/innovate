import { $django, useDjango } from "~/shared/django";
import { LoginInformation } from "~/shared/user";

export default defineEventHandler(async (event) => {
  // retrieve user data
  const info = await readBody<LoginInformation>(event);

  const { active } = useDjango();

  if (active) {
    // send request to django
    const resp = $django("/api/auth", {
      method: "POST",
      body: JSON.stringify(info),
    });

    if (resp.user) {
      await setUserSession(event, {
        user: resp.user,
      });

      // return {
      //     user: resp.user
      // }
    } else {
      // handle error
    }
  } else {
    throw createError({
      status: 501,
      message: "Server Unavailable",
    });
  }
});
