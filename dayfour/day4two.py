

def run_tests(file):
    rewards = {} 
    cards = {}
    final_rewards = {}
    with open(file, 'r') as f:
        while walrus := f.readline():
            game, reward = check_card(walrus)
            rewards[game] = reward
            cards[game] = 1
        
    final_rewards = check_dem_thingers(cards, rewards)
    final_count = final_tally(final_rewards)
    return final_count

def check_dem_thingers(ticket_count, rewards):
    tc = ticket_count.copy()
    
    for key in tc.keys():
        intkey = int(key)
        for i in range(1, tc[key] + 1):
            for i in range(1, rewards[key] + 1):
                tc[str(intkey + i)] += 1
    
    return tc 
            
def check_card(card):
    found_numbers = []
    i1 = card.find(':')
    i2 = card.find('|')


    numbers = card[i1+1:i2].split()
    scratch = card[i2+1:].split()
    game = card[:i1].strip('Card ')

    for itch in scratch:
        if itch in numbers:
            found_numbers.append(itch)

    return game, len(found_numbers)

def make_rewards(game, wins):
    rewards = []
    for i in range(1, wins):
        rewards.append(str(int(game) + i))
    return rewards
        
def final_tally(results):
    total = 0
    for v in results.values():
        total += v
    return total



print(run_tests('day4.txt'))
