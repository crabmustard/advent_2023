import re
card1 = 'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53'
card2 = 'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19'
card3 = 'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1'
card4 = 'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83'
card5 = 'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36'
card6 = 'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'


def run_tests(file):
    total_points = 0
    with open(file, 'r') as f:
        while walrus := f.readline():
            add_to = check_card(walrus)
            print(add_to)
            total_points += add_to
    return total_points



def check_card(card):
    found_numbers = []
    index_1 = card.find(':')
    game = card[:index_1].strip('Card ')
    points = 1

    card = card[index_1+1:]
    index_1 = card.find('|')
    numbers_on_card = card[:index_1].strip().split(' ')
    scratched_numbers = card[index_1 + 1:].strip()
    scratched_numbers = re.sub(' +', ' ', scratched_numbers).split(' ')

    for scratch in scratched_numbers:
        if scratch in numbers_on_card:
            found_numbers.append(scratch)
    if not found_numbers:
        points = 0
    else:
        lfn = len(found_numbers)-1
        points = 2 ** lfn


    return points




print(run_tests('day4.txt'))




