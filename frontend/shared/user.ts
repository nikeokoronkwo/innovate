import { z } from "zod";

// interface for login data

export const loginValidator = z.object({
  email: z
    .string()
    .min(1, { message: "Email is required." })
    .email({ message: "Invalid email address." }),
  password: z.string().min(1, { message: "Password is required." }),
});

export type LoginInformation = z.infer<typeof loginValidator>;

const signupValidator = z.object({});
