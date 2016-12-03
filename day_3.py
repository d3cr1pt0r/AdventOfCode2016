import re

input = file('day_3.input', 'r').read()
parse = re.findall(r'([0-9]{1,4})\s*([0-9]{1,4})\s*([0-9]{1,4})', input)
triangles = 0

for match in parse:
    x = int(match[0])
    y = int(match[1])
    z = int(match[2])

    if (x + y) > z and (y + z) > x and (z + x) > y:
        triangles += 1

print triangles