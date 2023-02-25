// 객체 리터럴 방식의 함수 체이닝

const exampleObject = {
  name: "foo",
  sayName: () => {
    console.log(`My name is ${this.name}`);
  },
};

exampleObject.sayName();
console.log(exampleObject.hasOwnProperty("name"));
console.log(exampleObject.hasOwnProperty("nickName"));
exampleObject.sayNickName();
