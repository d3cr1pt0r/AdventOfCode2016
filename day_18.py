import sys

def isSafe(row, index):
    safe_tiles = [False, False, False]

    if index - 1 < 0:
        safe_tiles[0] = True
    else:
        safe_tiles[0] = row[index-1] == '.'
    if index + 1 >= len(row):
        safe_tiles[2] = True
    else:
        safe_tiles[2] = row[index+1] == '.'

    safe_tiles[1] = row[index] == '.'

    rule_1 = not safe_tiles[0] and not safe_tiles[1] and safe_tiles[2]
    rule_2 = not safe_tiles[1] and not safe_tiles[2] and safe_tiles[0]
    rule_3 = not safe_tiles[0] and safe_tiles[1] and safe_tiles[2]
    rule_4 = not safe_tiles[2] and safe_tiles[0] and safe_tiles[1]

    return not (rule_1 or rule_2 or rule_3 or rule_4)

def solve_recursive(input, rows, safe_spots=0):
    row_new = ''
    rows -= 1

    for i in range(len(input)):
        if isSafe(input, i):
            row_new += '.'
        else:
            row_new += '^'

    safe_spots += input.count('.')
    #print input
    if rows > 0:
        solve_recursive(row_new, rows, safe_spots)
    else:
        print safe_spots

def solve_iterative(input, rows):
    r = [input]
    index = 0
    safe_spots = 0
    while index < rows:
        row = r.pop(0)
        row_new = ''
        safe_spots += row.count('.')
        #print row
        for i in range(len(row)):
            if isSafe(row, i):
                row_new += '.'
            else:
                row_new += '^'
        r.append(row_new)
        index += 1
    print safe_spots

input = '.^^.^^^..^.^..^.^^.^^^^.^^.^^...^..^...^^^..^^...^..^^^^^^..^.^^^..^.^^^^.^^^.^...^^^.^^.^^^.^.^^.^.'
rows = 400000
solve_iterative(input, rows)