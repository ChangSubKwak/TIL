// 5.4.3.2 하나의 클로저가 여러 함수 객체의 스코프 체인에 들어가 있는 경우도 있다
// Quokka를 이용하여 테스트 해보기

const func = () => {
  let x = 1;
  return {
    func1: () => {
      console.log(++x);
    },
    func2: () => {
      console.log(-x);
    },
  };
};

const exam = func();
exam.func1();
exam.func2();
