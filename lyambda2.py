a = input()
b = input()
c = input()


def compare(d, e, f):
    if (d == e) and  (d == f):
        return 3

    elif (d == e) or (d == f) or (e == f):
        return 2
    else:
        return 0

print(compare(a, b, c))