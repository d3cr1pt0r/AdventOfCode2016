input = file('day_7.input', 'r').readlines()

def match_found(i, o):
    for om in o:
        for im in i:
            if om == im[1] + im[0] + im[1]:
                return True
    return False

def task_1():
    supports_tls = 0
    for line in input:
        line = line.strip()
        ib = False
        ob = False

        for i in range(len(line)-3):
            d = [line[i], line[i+1], line[i+2], line[i+3]]
            pattern_match = d[1] == d[2] and d[0] == d[3] and d[0] != d[1]

            if line[i] == '[':
                in_brackets = True
            if line[i] == ']':
                in_brackets = False

            if pattern_match and not in_brackets:
                ob = True
            if pattern_match and in_brackets:
                ib = True

        if not ib and ob:
            supports_tls += 1

    return supports_tls

def task_2():
    supports_ssl = 0
    for line in input:
        line = line.strip()
        out_match = []
        in_match = []

        for i in range(len(line) - 2):
            d = [line[i], line[i + 1], line[i + 2]]
            pattern_match = d[0] == d[2] and d[0] != d[1]

            if line[i] == '[':
                in_brackets = True
            if line[i] == ']':
                in_brackets = False

            if pattern_match and not in_brackets:
                out_match.append(''.join([d[0], d[1], d[2]]))
            if pattern_match and in_brackets:
                in_match.append(''.join([d[0], d[1], d[2]]))

        if match_found(in_match, out_match):
            supports_ssl += 1

    return supports_ssl

print task_1()
print task_2()