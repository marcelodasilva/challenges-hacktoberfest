const intengers = [1, 2, 3 ,4, 5]
const sum = intengers.reduce((accumulate, currentValue) => accumulate + currentValue, 0);
const totalNumber = intengers.length
const result = sum / totalNumber
console.log(result)