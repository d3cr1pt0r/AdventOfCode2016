import hashlib

def md5(s):
    return hashlib.md5(s).hexdigest()

def isValidPosition(x, y):
    return x >= 0 and x < 4 and y >= 0 and y < 4

def getPossibleOptions(x, y, input):
    hash = md5(input)
    open_chars = ['b', 'c', 'd', 'e', 'f']
    options = []

    if hash[0] in open_chars and isValidPosition(x, y - 1):
        options.append(('U', (x, y - 1)))
    if hash[1] in open_chars and isValidPosition(x, y + 1):
        options.append(('D', (x, y + 1)))
    if hash[2] in open_chars and isValidPosition(x - 1, y):
        options.append(('L', (x - 1, y)))
    if hash[3] in open_chars and isValidPosition(x + 1, y):
        options.append(('R', (x + 1, y)))

    return options

input = 'pxxbnzuo'
queue = [(input, (0, 0), 0)]
visited = set()
max_dist = 0
path_found = False

while len(queue) > 0:
    data, pos, dist = queue.pop(0)

    if pos[0] == 3 and pos[1] == 3:
        if not path_found:
            path_found = True
            print 'Shortest path:', data.replace(input, '')
        max_dist = dist
        continue

    for d, np in getPossibleOptions(pos[0], pos[1], data):
        queue.append((data + d, np, dist + 1))

print 'Max distance:', max_dist