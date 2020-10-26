const randomArray = Array.from({length: 10}, () => Math.floor(Math.random() * 100));
const sum = randomArray.reduce((x, y) => x + y, 0)


console.log(`Array: ${randomArray}\nSum of elements: ${sum}`)




