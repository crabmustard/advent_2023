def get_file(file):
    f = open(file, 'r').read().split()
    return f
    
def make_grid(list_file):
    grid = list_file    
    checker = []
    for i in range(len(grid)):
        for k in range(len(grid[i])):
            if grid[i][k] == '#':
                checker.append([i, k])
    xset = set()
    yset = set()
    ref_set = set(i for i in range(len(grid)))
    for i in checker:
        yset.add(i[0])
        xset.add(i[1])

    # lists of empty rows and columns to use when calculating expansion
    diff = [list(ref_set.difference(yset)), list(ref_set.difference(xset))]
    
    return grid, checker, diff

# gets the distance and any crossings over expansion
def get_distance(g1, g2, diffs):
    millions = 0
    y1, y2, x1, x2 = g1[0], g2[0], g1[1], g2[1]
    ydel = abs(y2 - y1)
    xdel = abs(x2 - x1)
    for i in diffs[0]:
        if min(y2,y1) < i < max(y2, y1):
            millions += 1
    for j in diffs[1]:
        if min(x2, x1) < j < max(x2, x1):
            millions += 1
    return ydel + xdel, millions

def check_distances(galaxy, diffs):
    distances = []
    for k in galaxy:
        for i in range(1, len(galaxy)):
            distances.append(get_distance(k, galaxy[i], diffs))
        galaxy = galaxy[1:]
    return distances

def sum_total(distances, mult):
    total = 0
    for i in distances:
        d1 = i[0]
        d2 = i[1]
        total += d1 + d2*mult
    return total


grid = get_file('day11.txt')
grid, galaxy, diffs = make_grid(grid)
after = check_distances(galaxy, diffs)
# 2nd parameter: 1 for test1, 999999 for test2
after2 = sum_total(after, 1)
print(after2)
