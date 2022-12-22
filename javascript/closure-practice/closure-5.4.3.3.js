// 5.4.3.3 루프 안에서 클로저를 활용할 때는 주의하자
// Quokka를 이용하여 테스트 해보기
/*
const countSeconds = (howMany) => {
  for (let i = 1; i <= howMany; i++) {
    setTimeout(() => {
      console.log(i);
    }, i * 1000);
  }
};
*/

// 문제 발생
const countSeconds = (howMany) => {
  for (var i = 1; i <= howMany; i++) {
    setTimeout(() => {
      console.log(i);
    }, i * 1000);
  }
};

const countSecondsSolution1 = (howMany) => {
  for (let i = 1; i <= howMany; i++) {
    setTimeout(() => {
      console.log(i);
    }, i * 1000);
  }
};

const countSecondsSolution2 = (howMany) => {
  for (let i = 1; i <= howMany; i++) {
    ((currentI) => {
      setTimeout(() => {
        console.log(currentI);
      }, currentI * 1000);
    })(i);
  }
};

countSeconds(3);
countSecondsSolution1(3);
countSecondsSolution2(3);
