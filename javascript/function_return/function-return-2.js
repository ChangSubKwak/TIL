// 생성자 함수는 리턴값 없어도 생성된 객체를 리턴한다

function noReturnConstructorPerson(name, age, gender) {
  this.name = name;
  this.age = age;
  this.gender = gender;
}

const person1 = new noReturnConstructorPerson("changsub", 30, "man");
console.log(person1);

// 리턴값 있으면 그 객체를 리턴
function returnConstructorPerson(name, age, gender) {
  this.name = name;
  this.age = age;
  this.gender = gender;

  return {
    name: "young-changsub",
    age: 20,
    gender: "man",
  };
}

const person2 = new returnConstructorPerson("changsub", 30, "man");
console.log(person2);

// 기본탑을 리턴하면 기본값 대신 생성한 객체를 리턴
function returnPrimitivePerson(name, age, gender) {
  this.name = name;
  this.age = age;
  this.gender = gender;

  return 100;
}

const person3 = new returnPrimitivePerson("changsub", 30, "man");
console.log(person3);
