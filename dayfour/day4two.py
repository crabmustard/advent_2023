import re


def run_tests(file):
    reward_options = {} 
    card_count = {}
    final_rewards = {}
    with open(file, 'r') as f:
        while walrus := f.readline():
            game, rewards = check_card(walrus)
            reward_options[game] = rewards
            card_count[game] = 1
        
    final_rewards = add_to_ralf(card_count, reward_options)
    final_count = final_tally(final_rewards)
    return final_count

def add_to_ralf(ticket_count, rewards):
    rw = rewards.copy()
    tc = ticket_count.copy()
    
    for key in tc.keys():
        intkey = int(key)
        for i in range(1, tc[key] + 1):
            for i in range(1, rw[key] + 1):
                tc[str(intkey + i)] += 1
    
    return tc 
            
def check_card(card):
    found_numbers = []
    index_1 = card.find(':')
    game = card[:index_1].strip('Card ')

    card = card[index_1+1:]
    index_1 = card.find('|')
    numbers_on_card = card[:index_1].strip().split(' ')
    scratched_numbers = card[index_1 + 1:].strip()
    scratched_numbers = re.sub(' +', ' ', scratched_numbers).split(' ')

    for scratch in scratched_numbers:
        if scratch in numbers_on_card:
            found_numbers.append(scratch)

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
