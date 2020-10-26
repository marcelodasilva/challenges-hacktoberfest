const randomNumbers = Array.from({length: 5}, () => Math.floor(Math.random() * 10))
const sum = randomNumbers.reduce((x, y) => x + y, 0)
const denominator = randomNumbers.length;
const mean = sum/denominator

console.log(`Numbers: ${randomNumbers}\nMean: ${mean}`)