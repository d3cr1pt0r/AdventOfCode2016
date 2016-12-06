import hashlib

def task_1():
    input = 'abbhdwsy'
    password_length = 8
    password = ''

    index = 0
    while len(password) < password_length:
        h = hashlib.md5(input + str(index)).hexdigest()
        index += 1
        if h[:5] == '00000':
            print 'Found character at index', index, 'with hash', h
            password += h[5]

    return password

def task_2():
    input = 'abbhdwsy'
    password_length = 8
    password = [0] * password_length
    characters_found = 0
    filled_positions = []

    index = 0
    while characters_found < password_length:
        h = hashlib.md5(input + str(index)).hexdigest()
        index += 1

        if h[:5] == '00000' and h[5].isdigit() and int(h[5]) < 8 and int(h[5]) not in filled_positions:
            print 'Character position:', h[5], 'Character:', h[6], 'Hash:', h, 'Index:', index
            characters_found += 1
            filled_positions.append(int(h[5]))
            password[int(h[5])] = h[6]

    return password

print task_1()
print task_2()
