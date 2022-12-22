function f1() {
  return this;
}

// f1() === window;

console.log(f1() === global);

function f2() {
  "use strict";
  return this;
}

console.log(f2() === undefined);
