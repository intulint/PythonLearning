# import random
#
# try:
#     x=int(3*random.random())
#     assert x==1 , 'nope'
# except AssertionError:
#     print('nope')
# print(4)

# temp=-10
# assert (temp>=0), "Colder than absolute zero"

# msg='hello there'
# myf=None
# try:
#     myf = open("file.txt", 'w')
#     myf.write('123456 ')
#     amount_written_byte=myf.write(msg)
# finally:
#     myf.close()
# print(amount_written_byte)
# with open("file.txt") as f:
#     print(f.read())
#
# try:
#     with open("file.txt") as f:
#         print(f.read())
# except:
#     raise

# with open('file.txt','r') as mf:
#     file=mf.readlines()
#     lenf=len(file)
#     for i in range(lenf):
#         temp=str(file[i])
#         if i<lenf-1:
#             print(temp[0]+str(len(temp)-1))
#         else:
#             print(temp[0]+str(len(temp)))

st = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# q = [100 * i for i in range(0, 21, 2)]
# print(q)
#
# t = 'Hello, me and me'
# t = t.replace('me', 'everyone', 1)
# print(t)
#
# print()
#
# s = '|'.join(['1', '2', '3'])
# print(s)
#
# print()
#
# print(t.startswith("He"))
# print(t.endswith('e'))
# print(t.upper())
# print(t.lower())
# print(t.split(' '))
#
# print()
#
# print(min(st))
# print(max(st))
# print(abs(-124))  #абсалютное от нуля
# print(sum(st))
# print(round(123.1234,1))
sl={1:3,4:2,5:4}


if all([i>-1 for i in st]):
    print('ALl larger than -1')
if any([i>0 for i in st]):
    print('at least one is ever')
for i in enumerate(sl):
    print(i)