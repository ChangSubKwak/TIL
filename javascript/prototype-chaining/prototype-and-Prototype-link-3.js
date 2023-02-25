// 생성자 함수로 프로토타입 체이닝

function Person(name, age, gender) {
  this.name = name;
  this.age = age;
  this.gender = gender;
}

const changsub = new Person("changsub", 30, "man");

console.log(changsub.hasOwnProperty("name"));
console.log(changsub.hasOwnProperty("age"));
console.log(changsub.hasOwnProperty("gender"));
console.log(changsub.hasOwnProperty("job"));

console.log(Person.prototype);
