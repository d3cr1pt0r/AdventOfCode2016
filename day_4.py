import re, operator

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

def decrypt(list, id):
    new_list = []
    for r in list:
        word = ''
        for l in r:
            word += chr((((ord(l) - 97) + (id % 26)) % 26) + 97)
        new_list.append(word)
    return new_list

def task_1(input):
    sum = 0

    for line in input:
        parse = re.findall(r'([a-z]*?)-|([0-9]{1,4})\[([a-z]*?)\]', line)

        room_letters = []
        most_common_letters = ''
        id = parse[-1][1]
        hash = parse[-1][2]
        room_name = [i[0] for i in parse[:-1]]

        for p in room_name:
            for r in p:
                incrementListLetter(room_letters, r)

        t = sorted(room_letters, key=operator.itemgetter(0), reverse=False)
        t = sorted(t, key=operator.itemgetter(1), reverse=True)

        for i in t[:5]:
            most_common_letters += i[0]

        if most_common_letters == hash:
            sum += int(id)

    return sum

def task_2(input):

    for line in input:
        parse = re.findall(r'([a-z]*?)-|([0-9]{1,4})\[([a-z]*?)\]', line)

        id = parse[-1][1]
        room_name = [i[0] for i in parse[:-1]]

        room_name_d = decrypt(room_name, int(id))

        for name in room_name_d:
            if 'north' in name:
                return [room_name_d, id]

    return None

input = file('day_4.input', 'r').readlines()
print task_1(input)
print task_2(input)