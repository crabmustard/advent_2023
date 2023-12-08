def read_file(file):
    with open(file, 'r') as f:
        nodes = f.readlines()
        f.close()
    instructions = nodes[0].strip()
    node_list = {}
    for i in nodes[2:]:
        node = i[:3]
        left = i[7:10]
        right = i[12:15]
        node_list[node] = (left, right)
    return instructions, node_list

def run_game(file):
    inst, nodes = read_file(file)
    count = 0
    target = 'ZZZ'
    start = 'AAA'
    searching = True
    cur = start
    while searching is True:
        for i in inst:  
            if cur == target:
                searching = False
                break
            if i == "L":
                cur = nodes[cur][0]
                count += 1
            if i == "R":
                cur = nodes[cur][1]
                count += 1
    return count




print(run_game('day8.txt'))
