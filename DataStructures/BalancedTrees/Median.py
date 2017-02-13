#coding:utf-8
import bisect

N = int(raw_input())

array = []
for _ in range(N):
    operation, x = raw_input().split()
    if operation == 'a':
        #array.append(int(x))
        #array.sort()
        bisect.insort(array, int(x))
        length = len(array)
        if length % 2 == 0:
            index = length / 2 
            L = array[index-1]
            R = array[index]
            print (L+R) / 2.0 if (L+R) % 2 != 0 else (L+R) /2
        else:
            print array[length / 2] 
    elif operation == 'r':
        if array == [] or int(x) not in array:
            print 'Wrong!'
            continue
        array.remove(int(x))
        length = len(array)
        if length == 0:
            print 'Wrong!'
            continue
        if length % 2 == 0:
            index = length / 2 
            L = array[index-1]
            R = array[index]
            print (L+R) / 2.0 if (L+R) % 2 != 0 else (L+R) /2
        else:
            print array[length / 2] 
