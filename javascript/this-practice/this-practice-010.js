// 함수가 객체의 프로퍼티 값이면 메소드로서 호출된다.
// 이때 메소드 내부의 this는 해당 메소드를 소유한 객체, 즉 해당 메소드를 호출한 객체에 바인딩된다.

var obj1 = {
  name: "Lee",
  sayName: function () {
    console.log(this.name);
  },
};

var obj2 = {
  name: "Kim",
};

obj2.sayName = obj1.sayName;

obj1.sayName();
obj2.sayName();
