// 유사 배열 객체에서 배열 메서드를 사용하기

function useArrayMethod() {
  console.dir(arguments);
  const slicedArguments = Array.prototype.slice.apply(arguments, [1, 2]);

  // const slicedArguments = arrayArguments.slice(1);
  console.dir(slicedArguments);
}

useArrayMethod(1, 2, 3);
