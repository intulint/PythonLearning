# def alphabet_position(text):
#     ret=''
#     text=text.lower()
#     for i in range(len(text)):
#         if (ord(text[i])<65)or(ord(text[i])>122):
#             continue
#         else:
#             ret+=' '+str((ord(text[i])-96))
#     ret=ret[1::]
#     return ret
# x=alphabet_position("The sunset sets at twelve o' clock.")
# print(x)

# dat=[[18, 20],[45, 2],[61, 12],[37, 6],[21, 21],[78, 7]]
# def open_or_senior(data):
#     t=[]
#     for i in data:
#         if i[0]>=55 and i[1]>=7:
#             t.append('Senior')
#         else:
#             t.append('Open')
#     return t
# print(open_or_senior(dat))


# def song_decoder(song):
#     song=song.split('WUB')
#     t=song.copy()
#     for i in song:
#         if i=='':
#             t.remove(i)
#             print(t)
#     t=' '.join(t)
#     return print(song)
#
# song_decoder("AWUBWUBWUBBWUBWUBWUBC")

# def sum_two_smallest_numbers(numbers):
#     if len(numbers)>=4:
#         x=min(numbers)
#         numbers.remove(x)
#         return print(x+min(numbers))
#
# print(sum_two_smallest_numbers([5, 8, 12, 18, 22]))
# def pig_it(text):
#     word = text.split()
#     temp=[]
#     for i in word:
#         if i.isalpha():
#             temp.append(i[1:]+i[0]+'ya')
#         else:
#             temp.append(i)
#     print(' '.join(temp))
#
#
# pig_it('Pig latin is cool !')
#

# def anagrams(word, words):
#     temp=[]
#     for i in words:
#         if sorted(word)==sorted(i):
#             temp.append(i)
#     return print(temp)
#
# print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))

# def duplicate_encode(word):
#     word = word.lower()
#     res=''
#     for i in word:
#         if word.count(i)>1:
#             res+=')'
#         else:
#             res+='('
#     print(res)
#
# print(duplicate_encode('recede'))
# print(duplicate_encode('11123'))

# def expanded_form(num):
#     num = str(num)
#     dec=[]
#     for i in range(len(num)):
#         if num[i] == "0":
#             continue
#         dec.append(num[i] + '0' * (len(num) - i - 1))
#     return ' + '.join(dec)
#
#
# print(expanded_form(12))  # Should return '10 + 2'
# print(expanded_form(42))  # Should return '40 + 2'
# print(expanded_form(70304))  # Should return '70000 + 300 + 4'

# def solution(number):
#     s=0
#     for i in range(3,number):
#         if i%3==0 or i%5==0:
#             s+=i
#             continue
#         elif i%5==0:
#             s+=i
#         elif i%3==0:
#             s+=i
#     print(s)
#
#
# print(solution(10),' = ', 23)
