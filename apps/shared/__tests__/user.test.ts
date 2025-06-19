import { describe, it, expect } from "vitest";
import { UserCreate } from "../user";

describe("User schema", () => {
  it("parses basic object", () => {
    const parsed = UserCreate.parse({ email: "a@b.com" });
    expect(parsed.email).toBe("a@b.com");
  });
});
