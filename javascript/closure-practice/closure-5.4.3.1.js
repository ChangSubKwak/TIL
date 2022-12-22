// 5.4.3.1 클로저의 프로퍼티값이 쓰기 가능하므로 그 값이 여러 번 호출로 항상 변할 수 있음에 유의해야 한다
// Quokka를 이용하여 테스트 해보기

const outerFunc = (argNum) => {
  let num = argNum;
  return (x) => {
    num += x;
    console.log("num: " + num);
  };
};

const exam = outerFunc(40);
exam(5);
exam(-10);
