def find_diff_left(in_list, total):
    run_total = total
    if all([d == 0 for d in in_list]):
        in_list.insert(0, 0)
        return in_list, run_total
    else: 
        diffs = [in_list[i] - in_list[i-1] for i in range(1, len(in_list))]
        f = find_diff_left(diffs, run_total)
        diff = in_list[0] - f[1]
        in_list.insert(0, diff)
        run_total += diff
        return in_list, run_total

def find_diff_right(in_list, total):
    run_total = total
    if all([d == 0 for d in in_list]):
        in_list.append(0)
        return in_list, run_total
    else: 
        diffs = [in_list[i] - in_list[i-1] for i in range(1, len(in_list))]
        f = find_diff_right(diffs, run_total)
        diff = in_list[-1] + f[-1]
        in_list.append(diff)
        run_total += diff
        return in_list, run_total

def test_one(file):
    final_list = []
    data = open(file, 'r').readlines()
    for i in range(len(data)):
        current = [int(l) for l in data[i].strip().split()]
        final_list.append(find_diff_right(current, 0)[1])
    final_tally = 0
    for i in final_list:
        final_tally += i
    return final_tally

def test_two(file):
    final_list = []
    data = open(file, 'r').readlines()
    for i in range(len(data)):
        current = [int(l) for l in data[i].strip().split()]
        final_list.append(find_diff_left(current, 0)[1])
    final_tally = 0
    for i in final_list:
        final_tally += i
    return final_tally


t1 = test_one('day9.txt')
t2 = test_two('day9.txt')
print(f'Part one: {t1}\nPart two: {t2}')