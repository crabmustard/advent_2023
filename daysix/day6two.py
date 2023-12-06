race1 = 71530
dist1 = 940200
race2 = 55826490
dist2 = 246144110121111

def find_possible(time, record):
    first = int(record/time)
    last = time - first * 2
    min_time = 0
    max_time = 0
    for mi in range(0, first * 2):
        trav = mi * (time - mi)
        if trav > record:
            min_time = mi
            break
    for ma in range(last, time):
        trav = ma * (time - ma)
        if trav < record:
            max_time = ma
            break

    return max_time - min_time


print(find_possible(race1, dist1))