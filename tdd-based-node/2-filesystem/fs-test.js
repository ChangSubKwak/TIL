const fs = require('fs');

const rawData = fs.readFileSync('./data.txt');
console.log("rawData", rawData);

const data = fs.readFileSync('./data.txt', 'utf8');
console.log("data", data);