import random

v = []
for i in range(10):
    v.append(random.randint(1,9000))

sum = 0
for i in v:
    sum+=i

print(sum)
