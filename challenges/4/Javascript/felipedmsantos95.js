let fahrenheit = parseFloat(prompt('Enter a temperature in Fahrenheit:'))

let celsius = (fahrenheit - 32) * 5.0/9.0

console.log(`Temperature Fahrenheit: ${fahrenheit}º F\nTemperature Celsius: ${celsius.toFixed(2)}º C`)