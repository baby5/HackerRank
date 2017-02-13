#coding:utf-8

p = int(raw_input())
q = int(raw_input())

array = []
for i in xrange(p, q+1):
    if i == 1:
        array.append('1')
        continue

    sqr_str = str(i ** 2)
    num_length = len(str(i))
    sqr_length = len(sqr_str)

    if sqr_length > num_length:
        l = int(sqr_str[:num_length])
        r = int(sqr_str[num_length:])
        if r == 0:
            continue
        if l + r == i:
            array.append(str(i))
        else:
            l = int(sqr_str[:-num_length])
            r = int(sqr_str[-num_length:])
            if l + r == i:
                array.append(str(i))

if array:
    print ' '.join(array)
else:
    print 'INVALID RANGE' 
