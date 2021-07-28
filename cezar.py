# def rot13(message):
#     temp=''
#     # range(65,91)
#     # range(97,123)
#     for i in message:
#         if i.isalpha():
#             if i.isupper():
#                 if ord(i)<=78:
#                     temp+=chr(ord(i))
#                 else:
#                     temp+=chr(ord(i)-13)
#             elif i.lower():
#                 if ord(i)<=110:
#                     temp+=chr(ord(i))
#                 else:
#                     temp+=chr(ord(i)-13)
#         else:
#             temp +=i
#     return temp
#
#
# print(rot13("Test"))
import random


def recoverSecret(triplets):
    # temp = ['','','','','','','','','','']
    temp = []
    for i in triplets:
        t=0
        for n in i:
            if n in temp:
                t+=1
                continue
            temp.insert(t,n)
    t=0
    while True:
        for i in triplets:
            while True:
                m0=temp.index(i[0])
                m1=temp.index(i[1])
                m2=temp.index(i[2])
                if m0>m1:
                    temp[m0],temp[m1]=temp[m1],temp[m0]
                elif m1>m2:
                    temp[m1],temp[m2]=temp[m2],temp[m1]
                elif m0<m1<m2:
                    break
        t+=1
        if t>4:
            break
    return ''.join(temp)
    # print(temp)


secret = "whatisup"
triplets = [                 #01234567
    ['t', 'u', 'p'],  # 3,6,7 00010011
    ['w', 'h', 'i'],  # 0,1,4 11001000
    ['t', 's', 'u'],  # 3,5,6 00010110
    ['a', 't', 's'],  # 2,3,5 00110100
    ['h', 'a', 'p'],  # 1,2,7 01100001
    ['t', 'i', 's'],  # 3,4,5 00011100
    ['w', 'h', 's']   # 0,1,5 11000100
]
print(recoverSecret(triplets))

triplets2=\
[['t', 'in', 'f'],
 ['a', 'in', 'u'],
 ['m', 'a', 'f'],
 ['a', 'i', 'n'],
 ['in', 'u', 'n'],
 ['m', 'f', 'u'],
 ['a', 't', 'h'],
 ['t', 'h', 'i'],
 ['h', 'i', 'f'],
 ['m', 'h', 'f'],
 ['a', 'u', 'n'],
 ['m', 'a', 't'],
 ['f', 'u', 'n'],
 ['h', 'in', 'n'],
 ['a', 'and', 'in'],
 ['m', 'in', 'n'],
 ['m', 'in', 'u']]
print(recoverSecret(triplets2))