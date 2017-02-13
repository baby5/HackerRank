#coding:utf-8

for _ in range(input()):
    string = raw_input().strip()
    length = len(string)
    if length < 3:
        print "0"
        continue
    ind = 0 
    flag = 1
    while ind < length/2:
        if string[ind] == string[-1-ind]:
            ind+=1
        else:
            flag = 0
            break
    if flag == 1:
        print "-1"
        continue
    flag = 1
    spl = ind
    while ind<length/2:
        if string[ind] == string[-2-ind]:
            ind +=1
        else:
            flag = 0
            break
    if flag == 1:
        print length - 1 - spl
    else:
        print spl

'''
T = int(raw_input())

for _ in xrange(T):
    s = raw_input()

    i = 0
    j = len(s) - 1
    need_del = 0
    while i != j and i-j != 1:
        if s[i] != s[j]:
            need_del = 1
            break
        i += 1
        j -= 1

    if need_del:
        a = i+1
        b = j
        is_pal = 1
        while a != b and a-b != 1:
            if s[a] != s[b]:
                is_pal = 0
                break
            a += 1
            b -= 1
        if is_pal:
            print i
        else:
            is_pal = 1
            a, b = i, j-1
            while a != b and a-b != 1:
                if s[a] != s[b]:
                    is_pal = 0
                    break
                a += 1
                b -= 1
            if is_pal:
                print j
            else:
                print -1
    else:
        print -1
'''
