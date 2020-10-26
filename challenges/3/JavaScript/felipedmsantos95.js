let N = parseInt(prompt('Quantity of Fibonacci sequency numbers:'))

function fibonacci(num){
    var a = 1, b = 0, temp;
  
    while (num >= 0){
      temp = a;
      a = a + b;
      b = temp;
      num--;
    }
  
    return b;
}

for(let cont = 0; cont < N; cont++)
    console.log(fibonacci(cont))