from pprint import pprint
import string
sym_str = '''!"#$%&'()*+,-/:.;=<>?@[\\]^_`{|}~'''
no_dot = sym_str.replace('.','')
numstr = string.digits




def start_the_magic(file):
    finaltotal = 0
    foo = pad_file(file)
    bar = scan_list(foo)
    for index_pair in bar:
        bambam = check_around_symbols(foo, index_pair)
        for item in bambam:
            finaltotal += int(item)

    return finaltotal
    
        
    return final_list

def pad_file(file):
    new = []
    with open(file, 'r') as f:
        old = f.readlines()
        f.close()
    line_length = len(old[1])+ 5
    new.append('.' * (line_length))
    for i in range(len(old)):
        new.append(f'...{old[i].strip('\n')}...')
    new.append('.' * line_length)
    return new

def scan_list(in_list):
    symbol_idx = []
    for i in range(len(in_list)):
        for j in range(len(in_list[i])):
            if in_list[i][j] in no_dot:
                symbol_idx.append([i, j])
    return symbol_idx

def scan_line(in_line, counter):
    line_idx = []
    for j in range(len(in_line)):
        if in_line[j] in no_dot:
            line_idx.append([counter, j])
    return line_idx
    
def check_around_symbols(doc, pair):
    numbers_located = []
    i = pair[0]
    j = pair[1]
    top_l = doc[i-1][j-1]
    top_r = doc[i-1][j+1]
    top_c = doc[i-1][j]
    mid_r = doc[i][j+1]
    mid_c = doc[i][j]
    mid_l = doc[i][j-1]
    bot_l = doc[i+1][j-1]
    bot_c = doc[i+1][j]
    bot_r = doc[i+1][j+1]

    
    if top_c in numstr:
        if top_r in numstr and top_l not in numstr:
            numbers_located.append(doc[i-1][j:j+3].strip(sym_str).rstrip('.'))
        elif top_l in numstr and top_r not in numstr:
            numbers_located.append(doc[i-1][j-2:j+1].strip(sym_str).lstrip('.'))
        else:
            numbers_located.append(doc[i-1][j-2:j+2].strip(sym_str)) 
    if top_l in numstr and top_c not in numstr:
        numbers_located.append(doc[i-1][j-3:j].strip(sym_str).lstrip('.'))
    if top_r in numstr and top_c not in numstr:
        numbers_located.append(doc[i-1][j+1:j+4].strip(sym_str).rstrip('.')) 
    if mid_r in numstr:
        numbers_located.append(doc[i][j+1:j+4].strip(sym_str).rstrip('.'))
    if mid_l in numstr:
        numbers_located.append(doc[i][j-3:j].strip(sym_str).lstrip('.'))
    if bot_c in numstr:
        if bot_r in numstr and bot_l not in numstr:
            numbers_located.append(doc[i+1][j:j+3].strip(sym_str))
        elif bot_l in numstr and bot_r not in numstr:
            numbers_located.append(doc[i+1][j-2:j+1].strip(sym_str).lstrip('.'))
        else:
            numbers_located.append(doc[i+1][j-2:j+2].strip(sym_str))
    if bot_l in numstr and bot_c not in numstr:
        numbers_located.append(doc[i+1][j-3:j].strip(sym_str).rstrip('.'))
    if bot_r in numstr and bot_c not in numstr:
        numbers_located.append(doc[i+1][j+1:j+4].strip(sym_str).rstrip('.'))
            
    return numbers_located
    
    
tryto = start_the_magic('day3.txt')
print(tryto)