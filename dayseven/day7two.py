from collections import Counter
card_order = {'A': 14, 'K': 13, 'Q': 12, 'J': 1,
                'T': 10, '9': 9, '8': 8, '7': 7,
                 '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}

def change_card(card):
    return card_order[card]


def read_the_manual(file):
    strinput = open(file).readlines()
    c_input = []
    for i in strinput:
        i = i.split()
        i[0] = list(i[0])
        c_input.append(i)
    return c_input


def run_game(stuff_in):
    kind_5, kind_4, house_full, kind_3, pair_two, pair, high = [],[],[],[],[],[],[]
    for h in stuff_in:
        score = int(h[1])
        this = list(map(change_card, h[0]))
        c = Counter(this)
        if 1 in c:
            
            if len(c) > 1:
                tmp = c[1]
                del(c[1])
                print(c)
                mc = c.most_common(1)[0][0]
                c[mc] += tmp

        if len(c) == 1:
            kind_5.append([this, score])
        elif len(c) == 2:
            if c.most_common(1)[0][1] == 4:
                kind_4.append([this, score])
            else:
                house_full.append([this, score])
        elif len(c) == 3:
            if c.most_common(1)[0][1] == 3:
                kind_3.append([this, score])
            else:
                pair_two.append([this, score])
        elif len(c) == 4:
            pair.append([this, score])
        elif len(c) == 5:
            high.append([this, score])
        else:
            print('error ' + str(c) + ' ' + str(len(c)))

    ticker = len(stuff_in)
    print(ticker)
    total = 0
    print(len(kind_5) + len(kind_4) + len(kind_3) + len(house_full) + len(pair_two) + len(pair) + len(high))
    for hand in sorted(kind_5, reverse=True):
        total += hand[1] * ticker
        ticker -= 1
    for hand in sorted(kind_4, reverse=True):
        total += hand[1] * ticker
        ticker -= 1
    for hand in sorted(house_full, reverse=True):
        total += hand[1] * ticker
        ticker -= 1
    for hand in sorted(kind_3, reverse=True):
        total += hand[1] * ticker
        ticker -= 1
    for hand in sorted(pair_two, reverse=True):
        total += hand[1] * ticker
        ticker -= 1
    for hand in sorted(pair, reverse=True):
        total += hand[1] * ticker
        ticker -= 1
    for hand in sorted(high, reverse=True):
        total += hand[1] * ticker
        ticker -= 1
    print(ticker)

    return total



in_stuff = read_the_manual('day7.txt')
rasult = run_game(in_stuff)
print(rasult)


