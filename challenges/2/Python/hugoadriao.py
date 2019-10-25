from random import randint

size = randint(1,10)
values = [randint(1,20) for i in range(size)]
mean = sum(values)/len(values)

print(mean)