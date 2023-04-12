// setTimeout 이용한 삼수 사용자 정의
function callLater(obj, a, b) {
  return function () {
    obj["sum"] = a + b;
    console.log(obj["sum"]);
  };
}

let sumObj = {
  sum: 0,
};

const func = callLater(sumObj, 1, 2);

console.log("first", sumObj);
setTimeout(func, 500);
setTimeout(() => console.log("third", sumObj), 501);
