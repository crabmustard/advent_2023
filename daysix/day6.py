def run_race(time, record):
    time_held = 0
    max_time = time
    record = record
    speed = 0
    dist = 0
    valid = []
    for i in range(time_held, max_time):
        good = False
        time_held += 1
        speed += 1
        dist = (max_time - time_held) * speed
        if dist > record:
            valid.append([time_held, dist])
            good = True

    return len(valid)
    
race = 1    
race *= run_race(55, 246)
race *= run_race(82, 1441)
race *= run_race(64, 1012)
race *= run_race(90, 1111)
print(race)

