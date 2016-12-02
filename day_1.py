import math

def has_visited(x, y):
    for i in range(len(visited_x)):
        vx = visited_x[i]
        vy = visited_y[i]
        if vx == x and vy == y:
            return True
    return False

def distance(x, y):
    return abs(x) + abs(y)

input = "L2, L3, L3, L4, R1, R2, L3, R3, R3, L1, L3, R2, R3, L3, R4, R3, R3, L1, L4, R4, L2, R5, R1, L5, R1, R3, L5, R2, L2, R2, R1, L1, L3, L3, R4, R5, R4, L1, L189, L2, R2, L5, R5, R45, L3, R4, R77, L1, R1, R194, R2, L5, L3, L2, L1, R5, L3, L3, L5, L5, L5, R2, L1, L2, L3, R2, R5, R4, L2, R3, R5, L2, L2, R3, L3, L2, L1, L3, R5, R4, R3, R2, L1, R2, L5, R4, L5, L4, R4, L2, R5, L3, L2, R4, L1, L2, R2, R3, L2, L5, R1, R1, R3, R4, R1, R2, R4, R5, L3, L5, L3, L3, R5, R4, R1, L3, R1, L3, R3, R3, R3, L1, R3, R4, L5, L3, L1, L5, L4, R4, R1, L4, R3, R3, R5, R4, R3, R3, L1, L2, R1, L4, L4, L3, L4, L3, L5, R2, R4, L2"

x = 0
y = 0
angle = 0
dist = 0

visited_x = []
visited_y = []
visited_twice = False

spl = input.split(',')
for s in spl:
    s = s.strip()
    dir = s[0]
    num = int(s[1:])

    if dir == 'L':
        angle -= 90
    if dir == 'R':
        angle += 90

    if angle == 360:
        angle = 0
    if angle < 0:
        angle = 270

    d_x = int(math.cos(math.radians(angle)))
    d_y = int(math.sin(math.radians(angle)))

    for i in range(num):
        x += d_x
        y += d_y

        if has_visited(x, y) and not visited_twice:
            visited_twice = True
            print 'Visited twice:', distance(x, y), x, y

        visited_x.append(x)
        visited_y.append(y)

dist = distance(x, y)
print 'Final result:', dist, x, y