def increment_string(strng):
    if len(strng)==0 or strng[-1].isalpha():
        return strng+'1'
    if strng[-1].isdigit():
        temp=[]
        for i in strng[::-1]:
            if i.isdigit():
                temp.append(i)
                strng=strng[:len(strng)-1]
            else:
                break
        t=''.join(temp[::-1])
        for i in t:
            if i=='0':
                strng=strng+'0'
                t=t[1:]
            if i!='0':
                break
        if len(t) == 0:
            t = t + '0'
            strng = strng[:len(strng) - 1]
        if t.count('9')==len(t) and strng[-1]=='0':
            strng=strng[:len(strng)-1]
        t=int(t)+1
        return strng+str(t)


    # print(temp)
r='.={xKv[b_7384!W=M+;Q:12306A;Sk<TwCX122518693?o39218452g*]Zl3_C666B535758W|q@tL00000000010'
rr=increment_string(r)
print('\n',r,'\n',rr,'\n')


r='foobar00'
rr=increment_string(r)
print('\n',r,'\n',rr,'\n')

r='00000000573942850'
rr=increment_string(r)
print('\n',r,'\n',rr,'\n')

r='000000101960'
rr=increment_string(r)
print('\n',r,'\n',rr,'\n')
