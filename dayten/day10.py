def make_grid(file):
    tile_grid = open(file, 'r').read().split()
    s1 = None
    for i in range(len(tile_grid)):
        if "S" in tile_grid[i]:
            s1 = [i, tile_grid[i].find('S')]
    if s1 is None:
        print('No start found')
    return tile_grid, s1

print(make_grid('day10short.txt'))
test_grid , start = make_grid('day10short.txt')
sy, sx = start[0], start[1]
test_grid2 , start2 = make_grid('day10.txt')
sy2, sx2 = start2[0], start2[1]

def find_next(grid, y, x, d):

    square = grid[y][x]

    sx = x
    sy = y
    nd = d
    if d == 'u':
        if square == '|':
            nd = 'u'
            sy -= 1
        elif square == '7':
            nd = 'l'
            sx -= 1
        elif square == 'F':
            nd = 'r'
            sx += 1
    elif d == 'd':
        if square == '|':
            sy += 1
            nd = 'd'
        elif square == 'J':
            nd = 'l'
            sx -= 1
        elif square == 'L':
            nd = 'r' 
            sx += 1
    elif d == 'l':
        if square == '-':
            nd = 'l'
            sx -= 1
        elif square == 'F':
            nd = 'd'
            sy += 1
        elif square == 'L':
            nd = 'u'
            sy -= 1
    elif d == 'r':
        if square == '-':
            nd = 'r'
            sx += 1
        elif square == '7':
            nd = 'd'
            sy += 1
        elif square == 'J':
            nd = 'u'
            sy -= 1
    return nd, sy, sx
    
def traverse_loop(grid, y, x):
    print(grid[y][x])
    diffs = []

    found = False
    ny = y
    nx = x
    nd = 'd'
    counter = 0
    while not found:
        apy = abs((y-ny)) + abs((x-nx))
        diffs.append([apy, counter])
        cur = grid[ny][nx]
        if cur == 'S':
            if counter > 3:
                found = True
                break
            else:
                ny = y+1
            nd = 'd'
        nd, ny, nx = find_next(grid, ny, nx, nd)
        counter += 1

    return cur, diffs

        
step_count, diffs = traverse_loop(test_grid2, sy2, sx2)
    






test_grid , start = make_grid('day10short.txt')
sy, sx, sxt = start[0], start[1], 'd'
nxt, ny, nx = find_next(test_grid, sy, sx, sxt)
