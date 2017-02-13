#coding:utf-8

n, k = map(int, raw_input().split())
num = raw_input()

if n == 1:
    if k:
        print 9
    else:
        print num
else:
    cha_set = set()
    is_possible = 1
    half = n / 2
    mid = num[half] if n%2 != 0 else '' 
    left = list(num[:half])
    right = list(num[-half:])
    if k >= n:
        print '9'*n
    else:    
        for i in xrange(half):
            if left[-i-1] != right[i]:
                if k:
                    cha_set.add(i)
                    if left[-i-1] > right[i]:
                        right[i] = left[-i-1]
                    else:
                        left[-i-1] = right[i]
                    k -= 1
                else:
                    print -1
                    is_possible = 0
                    break   
        if is_possible:
            '''
            if k == 0:
                if left != right[::-1]:
                    print -1
                else:
                    print ''.join(left+[mid]+right)
            elif k == 1:
                if left[0] > right[-1]:
                    right[-1] = left[0]
                else:
                    left[0] = right[-1]
                if mid: mid = '9'
                print ''.join(left+[mid]+right)
            else:
            ''' 
            for i in xrange(half):
                r_i = half-1-i
                if k and left[i] != '9':
                    if k >= 2 and r_i not in cha_set:
                        left[i] = right[-i-1] = '9'
                        k -= 2
                    elif r_i in cha_set:
                        left[i] = right[-i-1] = '9'
                        k -= 1
            
            if k == 1 and mid: mid = '9'
            print ''.join(left+[mid]+right)
                
                      
