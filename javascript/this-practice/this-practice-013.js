// 생성자 함수 동작 방식
function Person(name) {
  // 생성자 함수 코드 실행 전 -------- 1
  this.name = name; // --------- 2
  // 생성된 함수 반환 -------------- 3
}

var me = new Person("Lee");
console.log(me.name);
