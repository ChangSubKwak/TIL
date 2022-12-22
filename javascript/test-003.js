var foo = function () {
  console.dir(this);
};

// foo();
// console.log(window);
// console.log(this);

var obj = { foo: foo };
obj.foo();

var instance = new foo();

var bar = { name: "bar", age: 20 };
foo.call(bar);
foo.apply(bar);
foo.bind(bar)();
