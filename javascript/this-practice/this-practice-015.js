// 생성자 함수에 new 연산자를 붙이지 않고 호출할 경우

function Person(name) {
  // new없이 호출하는 경우, 전역객체에 name 프로퍼티를 추가
  this.name = name;
}

// 일반 함수로서 호출되었기 때문에 객체를 암묵적으로 생성하여 반환하지 않는다.
// 일반 함수의 this는 전역객체를 가리킨다.
var me = Person("Lee");

console.log(me); // undefined
console.log(window.name); // Lee
