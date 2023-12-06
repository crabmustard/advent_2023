from pprint import pprint



def make_nac(file):
    with open(file, 'r') as f:
        nac = f.read()
        f.close()
    return nac

def process_almanac(nac):
    new_a = list(filter(lambda x: len(x) > 0, nac.split('\n\n')))
    seeds, soil, fert, water, light, temp, hum, loc = new_a
    p_seeds = process_seeds(seeds)
    p_soil = process_next(soil)
    p_fert = process_next(fert)
    p_water = process_next(water)
    p_light = process_next(light)
    p_temp = process_next(temp)
    p_hum = process_next(hum)
    p_loc = process_next(loc)
    return p_loc
    


def process_seeds(seedline):
    linein = seedline
    colon = linein.find(':')
    seed_list = linein[colon + 1:].split()
    seed_list = [int(i) for i in seed_list] 
    return seed_list


def process_next(this_map):
    result_ranges = []
    colon = this_map.find(':')
    smp = this_map[colon + 1:].strip().split('\n')
    for i in range(len(smp)):
        smp[i] = smp[i].split()
        for j in range(len(smp[i])):
            smp[i][j] = int(smp[i][j])
    for sm in smp:
        result_ranges.append([[sm[1], sm[1] + sm[2]], sm[0]])
    return result_ranges

alm = make_nac('day5test.txt')

maybe = process_almanac(alm)
print(maybe)








