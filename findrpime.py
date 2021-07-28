from math import sqrt
import time

num = 1000

start = time.time()


def is_prime(num):  # its work
    if num <= 1:
        return 0
    else:
        n = int(sqrt(num))
        for i in range(2, n + 1):
            if num % i == 0:
                return i
        return


# f = open("file.txt", "w")
# for i in range(num):
#     f.write(str(is_prime(i)) + '\n')
# f.close()

# for i in range(num):
    # print(is_prime(i))
# temp1 = is_prime(num)

end = time.time()
print(end - start)

start = time.time()


def er(n):  # n - число, до которого хотим найти простые числа
    sieve = list(range(n + 1))
    sieve[1] = 0  # 1==false, без этой строки итоговый список будет содержать единицу
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    sieve=list(filter(lambda x: x!=0,sieve))
    return sieve


temp2 = er(num)
print(temp2)
end = time.time()
print(end - start)

# if temp2==temp1:
#     print('==')

# spf = []
# for i in sp:
#     if i != 0:
#         spf.append(True)
#     else:
#         spf.append(False)
#
# f = open('file.txt')
# right = None
# for i in spf:
#     if bool(i+1) == bool(f.readline()):
#         right = True
#         print(i)
# else:
#     right = False
#     print(i)
# f.close()
# print(right)
