import random

number_list = [random.randint(1, 1000) for i in range(10)]

print("Numbers :", number_list)
print("Sum :", sum(number_list))