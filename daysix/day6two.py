
race1 = 71530
dist1 = 940200
race2 = 55826490
dist2 = 246144110121111




def find_possible(time, record):
    ratio = int(record/time)
    first = ratio
    last = time - ratio * 2
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
            max_time = ma-1
            break

    return max_time, min_time


print(find_possible(race2, dist2))