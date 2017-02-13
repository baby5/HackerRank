#coding:utf-8

R, C, N = map(int, raw_input().split())

grid_1 = [[] for i in xrange(R)]

bomb_list = []
for i in xrange(R):
    row_list = list(raw_input())
    grid_1[i] = row_list
    for j in xrange(len(row_list)):
        if row_list[j] == 'O':
            bomb_list.append((i, j))

def is_vaild(x, y):
    return x >= 0 and x < R and y >= 0 and y < C# and (x, y) not in bomb_list 愚蠢至极！

def have_bomb(x, y, grid):
    if x+1 < R and grid[x+1][y] == 'O':
        return 1
    elif x-1 >= 0 and grid[x-1][y] == 'O':
        return 1
    elif y+1 < C and grid[x][y+1] == 'O':
        return 1
    elif y-1 >= 0 and grid[x][y-1] == 'O':
        return 1
    else:
        return 0

if N % 2 == 0:
    for _ in xrange(R):
        print ''.join(['O'] * C)
else:
    if N == 1:
        for row in grid_1:
            print ''.join(row)    
    else:
        while 1:
            grid_3 = [['O']*C for _ in xrange(R)] 
            for bomb in bomb_list:
                print bomb
                #middle
                x, y = bomb
                grid_3[x][y] = '.'
                
                #up
                i, j = x-1, y
                if is_vaild(i, j):
                    grid_3[i][j] = '.'
    
                #down
                i, j = x+1, y
                if is_vaild(i, j):
                    grid_3[i][j] = '.'
        
                #left
                i, j = x, y-1
                if is_vaild(i, j):
                    grid_3[i][j] = '.'
    
                #right
                i, j = x, y+1
                if is_vaild(i, j):
                    grid_3[i][j] = '.'
            
            if N/2 % 2 != 0:
                for row in grid_3:
                    print ''.join(row)
                break

            for i in xrange(R):
                row = []
                for j in xrange(C):
                    if grid_3[i][j] == 'O':
                        row.append('.')
                    elif have_bomb(i, j, grid_3):       
                        row.append('.')      
                    else:
                        row.append('O')
                print ''.join(row)

            break
