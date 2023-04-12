// 까먹기 쉬운 this 의 개념
// 같은 함수 내에 this가 있다 하더라도, 일단 함수 호출로 쓰일 때와, 생성자 함수로 쓰일 때가 달라진다.

const whatIsThis = function () {
  return this;
};

// 전역으로 정의된 this가 출력
console.log("--------------> 1", whatIsThis());

// 함수 내부의 this를 출력
console.log("--------------> 2", new whatIsThis());
