import hashlib, time

def task_1():
    input = 'abbhdwsy'
    password_length = 8
    password = ''

    index = 0
    while len(password) < password_length:
        h = hashlib.md5(input + str(index)).hexdigest()
        index += 1
        if h[:5] == '00000':
            print 'Character :', h[5], 'Hash:', h, 'Index:', index
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

        if h[:5] != '00000': continue
        if not h[5].isdigit(): continue
        if int(h[5]) >= 8: continue
        if int(h[5]) in filled_positions: continue

        pos = int(h[5])
        chr = h[6]

        print 'Position:', pos, 'Character:', chr, 'Hash:', h, 'Index:', index
        characters_found += 1
        filled_positions.append(pos)
        password[pos] = chr

    return ''.join(password)

t1_1 = time.time()
print task_1()
t1_2 = time.time()

t2_1 = time.time()
print task_2()
t2_2 = time.time()

print 'Task 1:', (t1_2 - t1_1) * 1000.0
print 'Task 2:', (t2_2 - t2_1) * 1000.0
print 'Together: ', (t2_2 - t1_1) * 1000.0