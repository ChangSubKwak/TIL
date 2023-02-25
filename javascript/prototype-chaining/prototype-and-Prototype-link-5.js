// this 바인딩 예제
function Person(name) {
  this.name = name;
}

Person.prototype.getName = function () {
  return this.name;
};

const foo = new Person("foo");
console.log(foo.getName());

Person.prototype.name = "directly set dummy";
console.log(Person.prototype.getName());
