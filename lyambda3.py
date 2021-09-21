import random
data = []

for i in range(10):
    data.append(random.randint(0, 100))


def sum_data(data_1):
    s = 0
    for j in data_1:
        s += j
    return s

print(data)
print(sum_data(data))
