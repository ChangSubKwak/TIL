// 5.4.2.1 특정함수에 사용자가 정의한 객체의 메서드 연결하기
// 예제 5-10
// Quokka를 이용하여 테스트 해보기

class HelloFunc {
  constructor(func) {
    this.greeting = "hello";
  }
  call(func) {
    func ? func(this.greeting) : this.func(this.greeting);
  }
}

const userFunc = function (greeting) {
  console.log(greeting);
};

let objHello = new HelloFunc();
objHello.func = userFunc;
objHello.call();

function saySomething(obj, methodName, name) {
  return function (greeting) {
    return obj[methodName](greeting, name);
  };
}

class newObj {
  constructor(obj, name) {
    obj.func = saySomething(this, "who", name);
    return obj;
  }

  who(greeting, name) {
    console.log(greeting + " " + (name || "everyone"));
  }
}

const testObj = new newObj(objHello, "changsub");
console.log(testObj);
testObj.call();
