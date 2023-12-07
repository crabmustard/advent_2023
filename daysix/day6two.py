import time
race1 = 71530
dist1 = 940200
race2 = 55826490
dist2 = 246144110121111


def run_race(time, record):
    first = int(record/time)
    last = time - first * 2
    min_time = 0
    max_time = 0
    mif = False
    maf = False
    for mi in range(first, first * 2):
        if mif == True:
            break
        else:
            trav = mi * (time - mi)
            if trav > record:
                min_time = mi
                mif = True
                break
    for ma in range(time - first, last, -1):
        if maf == True:
            break
        else:
            trav = ma * (time - ma)
            if trav > record:
                max_time = ma+1
                maf = True
                break
    return (max_time - min_time)

t1 = time.perf_counter_ns()
run_race(race2, dist2)
t2 = time.perf_counter_ns()
print(t2-t1)