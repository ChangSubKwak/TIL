// 5.4.2.1 특정함수에 사용자가 정의한 객체의 메서드 연결하기
// Quokka를 이용하여 테스트 해보기

function HelloFunc(func) {
  this.greeting = "hello";
}

HelloFunc.prototype.call = function (func) {
  console.log("func", func);
  console.log("this.greeting", this.greeting);
  console.log("this.func", this.func);

  func ? func(this.greeting) : this.func(this.greeting);
};

var userFunc = function (greeting) {
  console.log(greeting);
};

var objHello = new HelloFunc();
objHello.func = userFunc;
objHello.call();

// console.log(globalThis);
// console.log(this.globalThis);
// console.log(objHello.greeting);
// console.log(objHello.call());
