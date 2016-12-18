discs = {
    1: [13, 10],
    2: [17, 15],
    3: [19, 17],
    4: [7, 1],
    5: [5, 0],
    6: [3, 1],
    7: [11, 0], #uncomment this for part 2 of the assignment
}

def inc_pos(disc_index):
    discs[disc_index][1] += 1
    if discs[disc_index][1] >= discs[disc_index][0]:
        discs[disc_index][1] = 0

def will_be_zero(disc_index):
    n = discs[disc_index][1]
    for i in range(disc_index):
        n += 1
        if n >= discs[disc_index][0]:
            n = 0
    return n == 0

all_zero = False
time = 0

while not all_zero:
    all_zero = True
    for disc in discs:
        if not will_be_zero(disc):
            all_zero = False
        inc_pos(disc)

    time += 1

print time - 1
print discs