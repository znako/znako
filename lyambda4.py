import random
data = []


for i in range (20):
    data.append(random.randint(0, 20))

print(data)


def count_zero(data_1):
    k = 0
    for j in data_1:
        if j == 0:
            k += 1
    return k

print(count_zero(data))