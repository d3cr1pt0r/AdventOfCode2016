import math, time

def part_1():
    elves = []

    for i in range(3018458):
        elves.append([i+1, 1])

    while True:
        for j in range(len(elves)):
            if elves[j][1] == 0:
                continue

            elf_found = False
            elf_count = 1
            while elf_count < len(elves):
                next_elf_index = (j+elf_count) % len(elves)
                if elves[next_elf_index][1] != 0:
                    elf_found = True
                    break
                elf_count += 1

            if not elf_found:
                print elves[j]
                return

            elves[j][1] += elves[next_elf_index][1]
            elves[next_elf_index][1] = 0

def part_2():
    elves = {}

    for i in range(3018458):
        elves[i+1] = 1

    elves_keys = elves.keys()
    elves_index = 0
    while len(elves_keys) > 1:
        s = time.time()
        elf_index = elves_keys[elves_index]
        neighbour_elf_index = int(elves_index + math.floor(len(elves) / 2)) % len(elves)
        elves[elf_index] += elves[elves_keys[neighbour_elf_index]]

        elves.pop(elves_keys[neighbour_elf_index], None)
        elves_keys.remove(elves_keys[neighbour_elf_index])

        elves_index = elves_keys.index(elf_index)
        elves_index = (elves_index + 1) % len(elves)
        e = time.time()
        print (e-s)

    print elves_keys

#part_1()
part_2()