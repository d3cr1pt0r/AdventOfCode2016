import hashlib

def md5(s):
    return hashlib.md5(s).hexdigest()

def isValidPosition(x, y):
    return x >= 0 and x < 4 and y >= 0 and y < 4

def getPossibleOptions(x, y, input):
    hash = md5(input)
    open_chars = ['b', 'c', 'd', 'e', 'f']
    options = []

    if hash[0] in open_chars and isValidPosition(x, y-1):
        options.append('U')
    if hash[1] in open_chars and isValidPosition(x, y+1):
        options.append('D')
    if hash[2] in open_chars and isValidPosition(x-1, y):
        options.append('L')
    if hash[3] in open_chars and isValidPosition(x+1, y):
        options.append('R')

    return options

input = 'ihgpwlah'
path = []
vault_found = False
x = 0
y = 0

while not vault_found:
    options = getPossibleOptions(x, y, input)