import { describe, it, expect } from "vitest";
import { scoreRequest } from "../schemas";

describe("schemas", () => {
  it("parses score request", () => {
    const r = scoreRequest.parse({
      earnings: [1, 2],
      rating: 4.5,
      tenure_months: 3,
    });
    expect(r.rating).toBe(4.5);
  });
});
