console.log(this === global);

var ga = "Global variable";

console.log(ga);
console.log(window.ga);

function foo() {
  console.log("invoked!");
}

foo();
