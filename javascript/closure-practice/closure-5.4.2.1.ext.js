// 5.4.2.1 특정함수에 사용자가 정의한 객체의 메서드 연결하기
//         인자가 두 개 이상인 함수를 사용하고자 할 때
// Quokka를 이용하여 테스트 해보기

function HelloFunc(func) {
  this.greeting = "hello";
}

HelloFunc.prototype.call = function (func) {
  // console.log("func", func);
  // console.log("this.greeting", this.greeting);
  // console.log("this.func", this.func);

  func ? func(this.greeting) : this.func(this.greeting);
};

const userFunc = function (greeting) {
  console.log(greeting);
};

const objHello = new HelloFunc();
objHello.func = userFunc;
objHello.call();

const saySomething = (obj, methodName, name) => {
  return (greeting) => {
    return obj[methodName](greeting, name);
  };
};

function newObj(obj, name) {
  // const newObj = (obj, name) => {
  obj.func = saySomething(this, "who", name);
  return obj;
}

// console.log(typeof newObj);

newObj.prototype.who = (greeting, name) => {
  console.log(greeting + " " + (name || "everyone"));
};

var obj1 = new newObj(objHello, "chang");
obj1.call();
