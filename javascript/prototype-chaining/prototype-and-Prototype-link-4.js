// 프로토타입에 자바스크립트 객체 할당
function Person(name) {
  this.name = name;
}

const foo = new Person("foo");

Person.prototype.sayHello = () => {
  console.log("Hello");
};

foo.sayHello();

const LambdaPerson = (name) => {
  this.name = name;
};

const foo2 = LambdaPerson("foo2");

LambdaPerson.prototype.sayHello = () => {
  console.log("Hello");
};

// 람다함수는 객체가 아닌 듯하다.
//foo2.sayHello();
