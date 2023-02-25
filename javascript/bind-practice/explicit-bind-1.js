function Person(name, age, gender) {
  this.name = name;
  this.age = age;
  this.gender = gender;
}

const foo = {};

Person.apply(foo, ["foo", 30, "man"]); // Person.call(foo, "foo", 30, "man"); 와 똑같음
console.log(foo);
