input = open('day_20.input', 'r').readlines()

l_1 = []

for line in input:
    line = line.strip()
    n1 = int(line.split('-')[0])
    n2 = int(line.split('-')[1])

    l_1.append((n1, n2))

l_1.sort()
print l_1
n = 0
i = 0
t = 0
while n < 2**32 and i < len(l_1):
    if n >= l_1[i][0]:
        if n <= l_1[i][1]:
            n = l_1[i][1] + 1
            i += 1
            continue
        i += 1
    else:
        print n
        n += 1
        t += 1

print t
print n