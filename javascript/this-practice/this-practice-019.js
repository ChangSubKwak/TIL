// 프로토타입의 메서드와 일반함수와의 this가 다른 문제 발생

function Person(name) {
  this.name = name;
}

Person.prototype.doSomething = function (callback) {
  if (typeof callback == "function") {
    // --------- 1
    callback();
  }
};

function foo() {
  console.log(this.name); // --------- 2
}

var p = new Person("Lee");
p.doSomething(foo); // undefined
