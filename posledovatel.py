# def max_sequence(arr):
#     if len(arr) == 0:
        # return 0
    # b = False
    # for i in arr:
    #     if i < 0:
    #         b = False
    #     else:
    #         b = True
    #         break
    # if b == False:
    #     return 0
    # a = [0, 0]
    # for i in range(0, len(arr)):
    #     for y in range(len(arr), 0, -1):
    #         a[0] = sum(arr[i:y])
    #         if a[0] > a[1]:
    #             a[0], a[1] = a[1], a[0]
    # return max(a)
#
#
# t = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# print(max_sequence(t))
# def listprime(firstnum,lastnum):  # n - число, до которого хотим найти простые числа
#     sieve = list(range(lastnum + 1))
#     sieve[1] = 0  # 1==false, без этой строки итоговый список будет содержать единицу
#     for i in sieve:
#         if i > 1:
#             for j in range(i + i, len(sieve), i):
#                 sieve[j] = 0
#     sieve=list(filter(lambda x: x>=firstnum,sieve))
#     return sieve
#
# def gap(g, m, n):
#     templist=listprime(m,n)
#     for i in range(len(templist)):
#         if templist[i+1]-templist[i]==g:
#             return [templist[i],templist[i+1]]
#     print(templist)
#
# print(gap(2,100,110))
from line_profiler_pycharm import profile

primelist={}
def listprime():  # n - число, до которого хотим найти простые числа
    global primelist
    lastnum=1100000
    if len(primelist)==0:
        sieve = list(range(lastnum + 1))
        sieve[1] = 0  # 1==false, без этой строки итоговый список будет содержать единицу
        for i in sieve:
            if i > 1:
                for j in range(i + i, len(sieve), i):
                    sieve[j]=0
        primelist=sieve

def gap(g, m, n):
    listprime()
    templist= list(filter(lambda x: x>0, primelist[m:n+1]))
    for i in range(len(templist)-1):
        if templist[i+1]-templist[i]==g:
            return [templist[i],templist[i+1]]

print(gap(2,100,110))