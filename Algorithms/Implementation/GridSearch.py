#coding:utf-8

for _ in xrange(int(raw_input())):
    R, C = map(int, raw_input().split())
    grid = []
    for _ in xrange(R):
        grid.append(raw_input())

    r, c = map(int, raw_input().split())
    patterns = [raw_input() for _ in xrange(r)]
   
    can_search = False
    for i in xrange(R):
        for j in xrange(0, C-c+1):
            if grid[i][j:j+c] == patterns[0]:
                if i + r <= R:
                    k = i
                    for pattern in patterns[1:]:
                        k += 1
                        if grid[k][j:j+c] != pattern:
                            break
                    else:
                        can_search = True

    if can_search:
        print 'YES'
    else:
        print 'NO'
    
