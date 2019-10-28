'''
solution extracted from https://www.programiz.com/python-programming/examples/fibonacci-sequence

'''


number_of_terms = 10



def fib(number_of_terms):
    n1 = 0
    n2 = 1
    count = 0
    if number_of_terms <= 0:
        print("Please enter a positive integer")
    elif number_of_terms == 1:
        print("Fibonacci sequence upto",number_of_terms,":")
        print(n1)
    else:
        print("Fibonacci sequence upto",number_of_terms,":")
    while count < number_of_terms:
        print(n1,end=' , ')
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1


fib(number_of_terms)
