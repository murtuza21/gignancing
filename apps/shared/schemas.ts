import { z } from "zod";

export const otpRequest = z.object({
  email: z.string().email().optional(),
  phone: z.string().optional(),
});

export const otpVerifyRequest = otpRequest.extend({
  code: z.string(),
});

export const tokenResponse = z.object({
  access_token: z.string(),
  refresh_token: z.string(),
});

export const scoreRequest = z.object({
  earnings: z.array(z.number()),
  rating: z.number(),
  tenure_months: z.number(),
});

export const scoreResponse = z.object({
  tier: z.string(),
  max_principal: z.number(),
});

export const loanCreate = z.object({
  principal: z.number(),
  interest_rate: z.number(),
  term_months: z.number(),
});

export const repaymentCreate = z.object({
  loan_id: z.number(),
  amount: z.number(),
  due_date: z.string(),
});
