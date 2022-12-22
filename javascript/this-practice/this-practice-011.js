// 프로토타입 객체도 메소드를 가질 수 있다.
// 프로토타입 객체 메소드 내부에서 사용된 this도 일반 메소드 방식과 마찬가지로 해당 메소드를 호출한 객체에 바인딩된다.

function Person(name) {
  this.name = name;
}

Person.prototype.getName = function () {
  return this.name;
};

var me = new Person("Lee");
console.log(me.getName());

Person.prototype.name = "Kim";
console.log(Person.prototype.getName());
