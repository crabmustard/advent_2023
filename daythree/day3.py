from pprint import pprint
import string
symbol_string = '''!"#$%&'()*+,-/:.;=<>?@[\\]^_`{|}~'''
symbol_no_dot = symbol_string.replace('.','')
numberstring = string.digits



def start_the_magic(file):
    finaltotal = 0
    foo = pad_file(file)
    bar = scan_list(foo)
    for index_pair in bar:
        bambam = check_around_symbols(foo, index_pair)
        for item in bambam:
            print(item)
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
            if in_list[i][j] in symbol_no_dot:
                symbol_idx.append([i, j])
    return symbol_idx

def scan_line(in_line, counter):
    line_idx = []
    for j in range(len(in_line)):
        if in_line[j] in symbol_no_dot:
            line_idx.append([counter, j])
    return line_idx
    
def check_around_symbols(doc, pair):
    numbers_located = []
    # print(pair)
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
    # print(f'{top_l} {top_c} {top_r}')
    # print(f'{mid_l} {mid_c} {mid_r}')
    # print(f'{bot_l} {bot_c} {bot_r}')
    
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
            
    return numbers_located
    
    
tryto = start_the_magic('day3.txt')
print(tryto)