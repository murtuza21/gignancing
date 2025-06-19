import { z } from "zod";

export const UserCreate = z.object({
  email: z.string().email(),
  phone: z.string().optional(),
});

export type UserCreate = any;
