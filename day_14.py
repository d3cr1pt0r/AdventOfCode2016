import hashlib, re

def md5(s):
    return hashlib.md5(s).hexdigest()

def md5_stretched(s):
    h = md5(s)
    for i in range(2016):
        h = md5(h)
    return h

def check(index, salt, char):
    for i in xrange(1, 1001):
        seed = salt + str(index + i)
        hash = md5(seed)
        p = char + '{5}'
        match = re.search(p, hash)

        if match is not None:
            return index + i
    return -1

def check_stretched(index, salt, char):
    for i in xrange(1, 1001):
        seed = salt + str(index + i)
        hash = md5_stretched(seed)
        p = char + '{5}'
        match = re.search(p, hash)

        if match is not None:
            return index + i
    return -1

salt = 'ngcjuoqr'
index = 0
keys = 0

while keys < 64:
    seed = salt + str(index)
    hash = md5(seed)
    match = re.search(r'(.)\1{2}', hash)

    if match is not None:
        if check(index, salt, match.group(0)[0]) != -1:
            keys += 1
            if keys == 64:
                print index

    index += 1

index = 0
keys = 0

while keys < 64:
    seed = salt + str(index)
    hash = md5_stretched(seed)
    match = re.search(r'(.)\1{2}', hash)

    if match is not None:
        if check_stretched(index, salt, match.group(0)[0]) != -1:
            keys += 1
            if keys == 64:
                print index

    index += 1