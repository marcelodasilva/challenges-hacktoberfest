# Given an array of 10 integers numbers generated randomly, find the sum of its elements.

from random import randint
array = []
sum = 0
for i in range(10):
    generated_value = randint(a= 1, b=50)
    if i % 2 == 0:
        array.append(generated_value)
    else:
        array.append(generated_value*2)
for v in array:
    sum = sum + v
print (array)
print (sum)
