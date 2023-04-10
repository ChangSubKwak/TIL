import { isValid } from "./LC0020_Valid_Parentheses";

test("example1", () => {
  expect(isValid("()")).toBe(true);
});

test("example2", () => {
  expect(isValid("()[]{}")).toBe(true);
});

test("example3", () => {
  expect(isValid("(]")).toBe(false);
});
