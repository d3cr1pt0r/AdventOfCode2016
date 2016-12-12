input = file('day_12.input', 'r').readlines()

registers = {
    'a': 0,
    'b': 0,
    'c': 0,
    'd': 0,
}
index = 0

def getValue(string):
    try:
        return {'is_register': False, 'value': int(string)}
    except:
        try:
            return {'is_register': True, 'value': registers[string]}
        except:
            return {'is_register': False, 'value': None}

def executeInstruction(command, p1, p2=None):
    v1 = getValue(p1)
    v2 = getValue(p2)

    if command == 'cpy':
        registers[p2] = v1['value']
        return 1
    if command == 'inc':
        registers[p1] += 1
        return 1
    if command == 'dec':
        registers[p1] -= 1
        return 1
    if command == 'jnz':
        if v1['value'] != 0:
            return v2['value']

    return 1

while index < len(input):
    line = input[index].strip()
    args = line.split(' ')
    p2 = None

    if len(args) > 2:
        p2 = args[2]

    index += executeInstruction(args[0], args[1], p2)
print registers