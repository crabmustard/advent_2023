from pprint import pprint
import string
symbol_string = '''!"#$%&'()*+,-/:.;=<>?@[\\]^_`{|}~'''
symbol_no_dot = symbol_string.replace('.','')
numberstring = string.digits


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
    numbers_located = []
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
    
    if top_c in numberstring:
        if top_r in numberstring and top_l not in numberstring:
            numbers_located.append(doc[i-1][j:j+3].strip(symbol_string).rstrip('.'))
        elif top_l in numberstring and top_r not in numberstring:
            numbers_located.append(doc[i-1][j-2:j+1].strip(symbol_string).lstrip('.'))
        else:
            numbers_located.append(doc[i-1][j-2:j+2].strip(symbol_string)) 
    
    if top_l in numberstring and top_c not in numberstring:
        numbers_located.append(doc[i-1][j-3:j].strip(symbol_string).lstrip('.'))
    if top_r in numberstring and top_c not in numberstring:
        numbers_located.append(doc[i-1][j+1:j+4].strip(symbol_string).rstrip('.')) 
    
    if mid_r in numberstring:
        numbers_located.append(doc[i][j+1:j+4].strip(symbol_string).rstrip('.'))
    if mid_l in numberstring:
        numbers_located.append(doc[i][j-3:j].strip(symbol_string).lstrip('.'))
    
    if bot_c in numberstring:
        if bot_r in numberstring and bot_l not in numberstring:
            numbers_located.append(doc[i+1][j:j+3].strip(symbol_string))
        elif bot_l in numberstring and bot_r not in numberstring:
            numbers_located.append(doc[i+1][j-2:j+1].strip(symbol_string).lstrip('.'))
        else:
            numbers_located.append(doc[i+1][j-2:j+2].strip(symbol_string))
    
    if bot_l in numberstring and bot_c not in numberstring:
        numbers_located.append(doc[i+1][j-3:j].strip(symbol_string).rstrip('.'))
    if bot_r in numberstring and bot_c not in numberstring:
        numbers_located.append(doc[i+1][j+1:j+4].strip(symbol_string).rstrip('.'))

    if len(numbers_located) ==2:
        return True, numbers_located
    else:
        return False, numbers_located

def final_check(numbers_located):
    if truth:
        result = numbers_located[1] * numbers_located[0]   

def it_a_process(file):
    ratio_total = 0
    schem = open_the_damn_file(file)
    gear_poss = scan_list(schem)
    for poss in gear_poss:

        possibility, numbers = check_around_symbols(schem, poss)
        if possibility:
            ratio = int(numbers[0]) * int(numbers[1])
            ratio_total += ratio
    return ratio_total


ihopeso = it_a_process('day3.txt')
print(ihopeso)