// 디폴트 프로토타입 변경하기
function Person(name) {
  this.name = name;
}

console.log("1", Person.prototype.constructor);

const foo = new Person("foo");
console.log("2", foo);

Person.prototype = {
  country: "Republic of Korea",
};
console.log("3", Person.prototype.constructor);

const bar = new Person("bar");
console.log("4", foo.country);
console.log("5", bar.country);
console.log("6", foo.constructor);
console.log("7", bar.constructor);
