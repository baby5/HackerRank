
p = int(raw_input())

for _ in xrange(p):
    a = set(list(raw_input()))
    b = set(list(raw_input()))

    for char in a:
        if char in b:
            print 'YES'
            break
    else:
        print 'NO'

    
