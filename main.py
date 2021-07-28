from random import randint


def randmas(num):
    ob = []
    for ir in range(num):
        ob.append(randint(1, num))
    return ob


n = 10
x = randmas(n)
y = randmas(n)
z = randmas(n)

lst = []
for i in range(n):
    m = x[i] * y[i] * z[i]
    lst.append(m)

for i in range(n):
    for j in range(i + 1, len(lst)):
        if lst[j] > lst[i]:
            lst[j], lst[i] = lst[i], lst[j]
            x[j], x[i] = x[i], x[j]
            y[j], y[i] = y[i], y[j]
            z[j], z[i] = z[i], z[j]
for e in range(n):
    print(lst[e], x[e], y[e], z[e], sep=' ')
