import re, operator

input = file('day_4.input', 'r').readlines()
sum = 0

def isLetterInSublist(list, letter):
    for i in range(len(list)):
        if list[i][0] == letter:
            return i
    return -1

def incrementListLetter(list, letter):
    index = isLetterInSublist(list, letter)
    if index != -1:
        list[index][1] += 1
    else:
        list.append([letter, 0])

for line in input:
    parse = re.findall(r'([a-z]*?)-|([0-9]{1,4})\[([a-z]*?)\]', line)

    room_letter_order = {}
    room_letters = []
    most_common_letters = ''
    id = parse[-1][1]
    hash = parse[-1][2]

    for p in parse[:-1]:
        room_name = p[0]
        for r in room_name:
            incrementListLetter(room_letters, r)

    t = sorted(room_letters, key=operator.itemgetter(0), reverse=False)
    t = sorted(t, key=operator.itemgetter(1), reverse=True)

    for i in t[:5]:
        most_common_letters += i[0]

    if most_common_letters == hash:
        sum += int(id)

print sum