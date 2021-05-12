from random import randint

value = []
total = 0

for i in range(10):
    value.append(randint(1, 9000))
    total += value[i]

print(f'{value}\n{total}')
