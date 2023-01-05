const div = document.createElement("div");
div.className = "foo";

console.log(div.outerHTML);

div.classList.remove("foo");
div.classList.add("anotherclass");

console.log(div.outerHTML);

div.classList.toggle("visible");
console.log(div.outerHTML);

let i = 9;
div.classList.toggle("visible", i < 10);
console.log(div.outerHTML);

i = 11;
div.classList.toggle("visible", i < 10);
console.log(div.outerHTML);

console.log(div.classList.contains("foo"));

div.classList.add("foo", "bar", "baz");
console.log(div.outerHTML);

div.classList.remove("foo", "bar", "baz");
console.log(div.outerHTML);

const cls = ["foo", "bar"];
div.classList.add(...cls);
console.log(div.outerHTML);

div.classList.remove(...cls);
console.log(div.outerHTML);

div.classList.add(...cls);
div.classList.replace("foo", "bar");
console.log(div.outerHTML);
