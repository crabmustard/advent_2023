card_order = {'A': 14, 'K': 13, 'Q': 12, 'J': 11,
                'T': 10, '9': 9, '8': 8, '7': 7,
                 '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}

def read_the_manual(file):
    strinput = open(file).readlines()
    c_input = []
    for i in strinput:
        i = i.split()
        i[0] = list(i[0])
        c_input.append(i)
    return c_input


def run_game(stuff_in):
    kind_5 = []
    kind_4 = []
    house_full = []
    kind_3 = []
    pair_two = []
    pair = []
    high = []
    counter = len(stuff_in)
    for h in stuff_in:
        score = h[1]
        this = h[0]
        for i in range(len(this)):
            this[i] = card_order[this[i]]
        hand_set = set()
        for i in this:
            hand_set.add(i)
        if len(hand_set) == 1:
            kind_5.append([this, int(score)])
        elif len(hand_set) == 4:
            pair.append([this, int(score)])
        elif len(hand_set) == 5:
            high.append([this, int(score)])
        elif len(hand_set) == 2:
            copied = sorted(this)
            if copied[1] == copied[3]:
                kind_4.append([this, int(score)])
            else:
                house_full.append([this, int(score)])
        elif len(hand_set) == 3:
            fn = False
            copied = sorted(this)
            for i in range(3):
                print(copied)
                if copied[i] == copied[i+1] == copied[i+2]:
                    kind_3.append([this, int(score)])
                    fn = True
            if fn == False:
                pair_two.append([this, int(score)])
        else: print(f'not_found {hand}')

    total = 0
    
    for hand in sorted(kind_5, reverse=True):
        total += hand[1] * counter
        counter -= 1
    for hand in sorted(kind_4, reverse=True):
        total += hand[1] * counter
        counter -= 1
    for hand in sorted(house_full, reverse=True):
        total += hand[1] * counter
        counter -= 1
    for hand in sorted(kind_3, reverse=True):
        total += hand[1] * counter
        counter -= 1
    for hand in sorted(pair_two, reverse=True):
        total += hand[1] * counter
        counter -= 1
    for hand in sorted(pair, reverse=True):
        total += hand[1] * counter
        counter -= 1
    for hand in sorted(high, reverse=True):
        total += hand[1] * counter
        counter -= 1

    return total


in_stuff = read_the_manual('day7.txt')
rasult = run_game(in_stuff)

print(rasult)

