import operator

input = file('day_6.input', 'r').readlines()

length = len(input[0].strip())
commons = [None] * length

for line in input:
    line = line.strip()
    for i in range(length):
        if commons[i] is None:
            commons[i] = {}
        if line[i] not in commons[i]:
            commons[i][line[i]] = 0
        commons[i][line[i]] += 1

password1 = ''
password2 = ''
for i in range(length):
    password1 += sorted(commons[i].items(), key=operator.itemgetter(1), reverse=True)[0][0]
    password2 += sorted(commons[i].items(), key=operator.itemgetter(1), reverse=False)[0][0]

print password1
print password2