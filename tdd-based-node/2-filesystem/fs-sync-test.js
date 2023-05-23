const fs = require('fs');

const data = fs.readFile('./data.txt', 'utf8', (err, data) => {
  console.log("1 - data", data); 
  console.log("1 - err", err);
});
console.log("2 - data", data);