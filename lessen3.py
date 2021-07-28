# def getinput():
#     return input('anything \n')
#
# def testinput(val):
#     try:
#         c=int(val)
#         return True
#     except (ValueError):
#         return False
#
# def strToint(g):
#     return int(g)
#
# def printint(r):
#     print('is ', r)
#
# i=getinput()
# if testinput(i):
#     printint(strToint(i))
# else:
#     print('Error')

# i=None
# while i!='0':
#     i=input("enter number simvol \n")
#     print(chr(int(i)))
# print('end')

# i=None
# print('Enter string')
# while i!='0':
#     i=input()
#     if len(i)>10:
#         print('Not more 10 chr')
#     elif i=='0':
#         print('end')
#     elif len(i)<=10:
#         print(i+((10-len(i))*'*'))

print('Enter 6 real numbers')
i=[]
for e in range(6):
    i.append(float(input(str(e+1)+' - ')))
print(i)
for t in range(6):
    for e in range(t+1,6):
        if i[t]>i[e]:
            i[t],i[e]=i[e],i[t]
print(i)
print(round(i[0],2),round(i[len(i)-1],2))