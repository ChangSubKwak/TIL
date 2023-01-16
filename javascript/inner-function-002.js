function parent() {
  let a = 100;
  let b = 200;

  function child() {
    let b = 300;
    console.log(a);
    console.log(b);
  }
  child();
}

parent();
child(); // error
