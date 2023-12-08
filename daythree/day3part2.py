from pprint import pprint
import string
sym_str = '''!"#$%&'()*+,-/:.;=<>?@[\\]^_`{|}~'''
numstr = string.digits


def open_the_damn_file(file):
    with open(file, 'r') as f:
        parse = f.readlines()
        f.close()

    for i in range(len(parse)):
        parse[i] = parse[i].strip()
        parse[i] = f'...{parse[i]}...'

    parse.insert(0, '.' * len(parse[0]))
    parse.append('.' * len(parse[0]))

    return parse

def scan_list(in_list):
    symbol_idx = []

    for i in range(len(in_list)):
        for j in range(len(in_list[i])):
            if in_list[i][j] in '*':
                symbol_idx.append([i, j])
    
    return symbol_idx

def check_around_symbols(doc, pair):
    f_nums = []
    # print(pair)
    i = pair[0]
    j = pair[1]
    
    top_l = doc[i-1][j-1]
    top_r = doc[i-1][j+1]
    top_c = doc[i-1][j]
    mid_r = doc[i][j+1]
    mid_l = doc[i][j-1]
    bot_l = doc[i+1][j-1]
    bot_c = doc[i+1][j]
    bot_r = doc[i+1][j+1]
    
    if top_c in numstr:
        if top_r in numstr and top_l not in numstr:
            f_nums.append(doc[i-1][j:j+3].strip(sym_str).rstrip('.'))
        elif top_l in numstr and top_r not in numstr:
            f_nums.append(doc[i-1][j-2:j+1].strip(sym_str).lstrip('.'))
        else:
            f_nums.append(doc[i-1][j-2:j+2].strip(sym_str)) 
    
    if top_l in numstr and top_c not in numstr:
        f_nums.append(doc[i-1][j-3:j].strip(sym_str).lstrip('.'))
    if top_r in numstr and top_c not in numstr:
        f_nums.append(doc[i-1][j+1:j+4].strip(sym_str).rstrip('.')) 
    
    if mid_r in numstr:
        f_nums.append(doc[i][j+1:j+4].strip(sym_str).rstrip('.'))
    if mid_l in numstr:
        f_nums.append(doc[i][j-3:j].strip(sym_str).lstrip('.'))
    
    if bot_c in numstr:
        if bot_r in numstr and bot_l not in numstr:
            f_nums.append(doc[i+1][j:j+3].strip(sym_str).rstrip('.'))
        elif bot_l in numstr and bot_r not in numstr:
            f_nums.append(doc[i+1][j-2:j+1].strip(sym_str).lstrip('.'))
        else:
            f_nums.append(doc[i+1][j-2:j+2].strip(sym_str))
    
    if bot_l in numstr and bot_c not in numstr:
        f_nums.append(doc[i+1][j-3:j].strip(sym_str).rstrip('.'))
    if bot_r in numstr and bot_c not in numstr:
        f_nums.append(doc[i+1][j+1:j+4].strip(sym_str).rstrip('.'))

    if len(f_nums) ==2:
        return True, f_nums
    else:
        return False, f_nums

def it_a_process(file):
    ratio_total = 0
    schem = open_the_damn_file(file)
    gear_poss = scan_list(schem)
    for poss in gear_poss:

        possibility, numbers = check_around_symbols(schem, poss)
        if possibility:
            ratio_total += int(numbers[0]) * int(numbers[1])

    return ratio_total


ihopeso = it_a_process('day3.txt')
print(ihopeso)