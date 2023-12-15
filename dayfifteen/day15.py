from collections import OrderedDict

def hash_seg(segment):
    hsh = 0
    for i in segment:
        hsh += ord(i)
        hsh *= 17
        hsh %= 256
    return hsh

def part1(input):
    total = 0
    for item in input:
        total += hash_seg(item)
    return total

code = open('day15.txt').read()
split = code.split(',')

main_dict = OrderedDict()
for line in split:
    if '=' in line:
        key = line[:-2]
        hsh = str(hash_seg(key))
        val = line[-1]
        if hsh not in main_dict:
            main_dict[hsh] = OrderedDict()
        if key not in main_dict[hsh]:
            main_dict[hsh][key] = -1
        main_dict[hsh][key] = val
    elif '-' in line:
        key = line[:-1]
        hsh = str(hash_seg(key))
        if hsh in main_dict:
            if key in main_dict[hsh]:
                main_dict[hsh].pop(key)

z = []
for hsh in main_dict.keys():
    cnt = 1
    for key in main_dict[hsh].keys():
        z.append([int(hsh)+1, int(main_dict[hsh][key]), cnt])
        cnt += 1

total = 0
for i in z:
    total += i[0] * i[1] * i[2]
p1 = part1(split)
print(f'Part 1: {p1}')
print(f'Part 2: {total}')
