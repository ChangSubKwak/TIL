const parent = () => {
  const a = 100;

  const child = () => {
    console.log(a);
  };
  return child;
};

const innerChild = parent();
innerChild();
