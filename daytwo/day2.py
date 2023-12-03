from pprint import pprint

red_cubes = 12
green_cubes = 13
blue_cubes = 14




def read_games(file):
    count = 0
    good_sum = 0
    bad_sum = 0
    good_games = []
    bad_games = []
    with open(file, 'r') as f:
        while load_line := f.readline():
            game_number, cleaned = clean_line(load_line)
            clean_draws = check_draws_possible(cleaned)
            pprint(cleaned)
            if clean_draws == True:
                good_sum += game_number
            count += 1
    print(f'read {count}')
    return good_sum, bad_sum, bad_games, good_games
            
def clean_line(line):
    colon = line.find(':')
    game_no = int(line[:colon].strip('Game'))
    cube_draws = []
    still_to_process = line[colon + 2:]
    still_to_process = still_to_process.split('; ')
    for i in range(len(still_to_process)):
        split_values = still_to_process[i]
        split_values = split_values.split(', ')
        for j in range(len(split_values)):
            split_values[j] = split_values[j].split(' ')
            split_values[j][0] = int(split_values[j][0])

        cube_draws.append(split_values)
    return game_no, cube_draws

def check_draws_possible(draw_list):
    for hand in draw_list:
        for grab in hand:
            color, adder = grab[1], grab[0]
            if color == 'red' and adder > red_cubes:
                return False
            if color == 'blue' and adder > blue_cubes:
                return False
            if color == 'green' and adder > green_cubes:
                return False


    return True

aberc, baberc, bad_aber, good_aber = read_games('day2.txt')    
print(aberc)

