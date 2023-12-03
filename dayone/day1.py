# callig read this on a file
# takes line by line, runs through a cleaner, optional int reducer, 
# parses the string for first and last int
# string concat on first and last int -> back to int
# sums the returned code value from string


numbers_zeronine = [str(i) for i in range(10)]
ref_len_three = ['one', 'two', 'six']
ref_len_four = ['four', 'five', 'nine']
ref_len_five = ['three', 'seven', 'eight']
ref_replacement = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',  'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

def read_dis(file):
    total_sum = 0
    with open(file, 'r') as f:
        while jerk := f.readline(): # reads line
            cleanline = switch_str_int(jerk)
            bad_clean = switch_str_int_didnt_work(jerk)
            if cleanline != bad_clean:
                print(f'heres an error: {cleanline[:-1]:.20}  |  {bad_clean[:-1]:.20}') # cleans
            # ints_only = drop_chars(cleanline) # integer character only for checking
            add_sum = get_code_from_string(cleanline) # parse int code from string
            total_sum += add_sum # add code sum to sum
    return total_sum

# def get_code_string(file):
#     numb = [str(i) for i in range(10)]
#     codes = []
#     total_sum = 0
#     with open(file, 'r') as f:
#         while line := f.readline():
#             fnum, lnum = 0,0
#             for letter in line:
#                 if letter in numb:
#                     fnum = letter
#                     break
#             for letter in line[::-1]:
#                 if letter in numb:
#                     lnum = letter
#                     break
#             codes.append(int(fnum + lnum))
#     for code in codes:
#         total_sum += code
#     return total_sum

def get_code_from_string(text):
    numb = [str(i) for i in range(10)]
    fnum, lnum = 0,0
    for letter in text:
        if letter in numb:
            fnum = letter
            break
    for letter in text[::-1]:
        if letter in numb:
            lnum = letter
            break
    return int(fnum + lnum)

def switch_str_int(instr): # finds and replaces str to strint
    low_str, i = instr.lower(), 0
    new_str = ''
    while i < len(low_str):
        if low_str[i:i+3] in ref_len_three:
            addto = ref_replacement[low_str[i:i+3]]
            new_str += addto
            i += 2
        elif low_str[i:i+4] in ref_len_four:
            addto = ref_replacement[low_str[i:i+4]]
            new_str += addto
            i += 3
        elif low_str[i:i+5] in ref_len_five:
            addto = ref_replacement[low_str[i:i+5]]
            new_str += addto
            i += 4
        else: 
            new_str += instr[i]
            i += 1
    return new_str
def switch_strip_int(instr): # finds and replaces str to strint
    low_str, i = instr.lower(), 0
    new_str = ''
    while i < len(low_str):
        if low_str[i:i+3] in ref_len_three:
            addto = ref_replacement[low_str[i:i+3]]
            new_str += addto
            i += 2
        elif low_str[i:i+4] in ref_len_four:
            addto = ref_replacement[low_str[i:i+4]]
            new_str += addto
            i += 3
        elif low_str[i:i+5] in ref_len_five:
            addto = ref_replacement[low_str[i:i+5]]
            new_str += addto
            i += 4
        else:
            if low_str in numbers_zeronine: 
                new_str += instr[i]
            i += 1
    return new_str

# def switch_str_int_didnt_work(instr): # finds and replaces str to strint
#     low_str, i = instr.lower(), 0
#     new_str = ''
#     while i < len(low_str):
#         if low_str[i:i+3] in ref_len_three:
#             addto = ref_replacement[low_str[i:i+3]]
#             new_str += addto
#             i += 3
#         elif low_str[i:i+4] in ref_len_four:
#             addto = ref_replacement[low_str[i:i+4]]
#             new_str += addto
#             i += 4
#         elif low_str[i:i+5] in ref_len_five:
#             addto = ref_replacement[low_str[i:i+5]]
#             new_str += addto
#             i += 5
#         else: 
#             new_str += instr[i]
#             i += 1
#     return new_str

def drop_chars(string):
    return_only_ints = ''
    for i in string:
        if i in numbers_zeronine:
            return_only_ints += i
    return return_only_ints
    