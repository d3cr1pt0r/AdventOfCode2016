import re

def isValidTriangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

input = file('day_3.input', 'r').read()
parse = re.findall(r'([0-9]{1,4})\s*([0-9]{1,4})\s*([0-9]{1,4})', input)
triangles = 0

for match in parse:
    x = int(match[0])
    y = int(match[1])
    z = int(match[2])

    if isValidTriangle(x, y, z):
        triangles += 1

print triangles
triangles = 0

for i in xrange(0, len(parse), 3):
    r_1_x = int(parse[i][0])
    r_1_y = int(parse[i + 1][0])
    r_1_z = int(parse[i + 2][0])

    r_2_x = int(parse[i][1])
    r_2_y = int(parse[i + 1][1])
    r_2_z = int(parse[i + 2][1])

    r_3_x = int(parse[i][2])
    r_3_y = int(parse[i + 1][2])
    r_3_z = int(parse[i + 2][2])

    if isValidTriangle(r_1_x, r_1_y, r_1_z):
        triangles += 1
    if isValidTriangle(r_2_x, r_2_y, r_2_z):
        triangles += 1
    if isValidTriangle(r_3_x, r_3_y, r_3_z):
        triangles += 1

print triangles