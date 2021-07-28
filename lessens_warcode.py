def count_bits(num):
    it = [num]
    x = []
    while True:
        f, it[0] = cikl(it[0])
        x.append(f)
        print(x[0], it[0])
        if it[0] == 1:
            x.append(1)
            break
        elif it[0] == 0:
            x.append(0)
            break
    return sum(x)


def cikl(num):
    new_num = 0
    x = 0
    if num == 1:
        new_num = 1
        x = 1
    elif num == 0:
        new_num = 0
        x = 0
    elif num >= 2:
        if num % 2 == 1:
            new_num = int((num - 1) / 2)
            x = 1
        elif num % 2 == 0:
            new_num = int(num / 2)
            x = 0
    return x, new_num

print(count_bits(40))

def count_bits2(num):
    return bin(num).count('1')

print(count_bits2(40))
