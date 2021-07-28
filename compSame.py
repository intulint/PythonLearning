# def productFib(prod):
#     fiblist = [0, 1]
#     while True:
#         f1=fiblist[len(fiblist) - 1]
#         f2=fiblist[len(fiblist) - 2]
#         if f1*f2==prod:
#             return f2,f1, True
#         elif f1*f2>prod:
#             return f2,f1, False
#         fiblist.append(f1+f2)
#
# x=list(productFib(5895))
# print(x)

# def productFib(prod):
#     a,b=0,1
#     while prod>a*b:
#         a,b=b,a+b
#     return [a,b,prod==a*b]
#
# x=list(productFib(5895))
# print(x)
CACHE = {}

def cash(i):
    if i not in CACHE:
        temp = [k for k in range(1, i + 1) if i%k==0]
        CACHE[i]=sum([x*x for x in temp])
        return CACHE[i]
    return CACHE[i]

def list_squared(m, n):
    ret = []
    for i in range(m, n + 1):
        temp = cash(i)
        if (temp**0.5).is_integer():
            ret.append([i, temp])
    return ret


x = list_squared(1, 250)
print(x)