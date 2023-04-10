/**
 * @param {string} s
 * @return {boolean}
 */
export function isValid(s) {
  let i = 0;
  let stack = [];
  for (let i = 0; i < s.length; i++) {
    if (["(", "[", "{"].includes(s[i])) {
      stack.push(s[i]);
      continue;
    }

    const topElement = stack.pop();
    if (s[i] === ")" && topElement !== "(") {
      return false;
    }

    if (s[i] === "]" && topElement !== "[") {
      return false;
    }

    if (s[i] === "}" && topElement !== "{") {
      return false;
    }
  }

  if (stack.length > 0) {
    return false;
  }

  return true;
}
