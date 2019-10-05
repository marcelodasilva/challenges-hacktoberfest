def Fibonacci(n): 
    if n==1: 
        return 0
    elif n==2: 
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2) 
  
n=int(input("Enter integer greater than 0: "))

if n<1:
    print("Please enter integer greater than 0.")
else:
    print("Fibonacci sequence upto",n,"terms: ")
    for i in range(1,n+1):
        print(Fibonacci(i),end=" ") 
