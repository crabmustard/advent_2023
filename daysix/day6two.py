race1 = 71530
dist1 = 940200
race2 = 55826490
dist2 = 246144110121111



# improper loop, doesn't fully break ~.5 seconds


# def find_possible(time, record):
#     first = int(record/time)
#     last = time - first * 2
#     min_time = 0
#     max_time = 0
#     for mi in range(first, first * 2):
#         trav = mi * (time - mi)
#         if trav > record:
#             min_time = mi
#             break
#     for ma in range(last, time-first):
#         trav = ma * (time - ma)
#         if trav < record:
#             max_time = ma
#             break
#     return (max_time - min_time)



def find_possible_rev(time, record):
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


print(find_possible_rev(race2, dist2))