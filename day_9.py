def decompressedLength(string, recurive=False):
    p_start = -1
    p_end = -1
    p_in = False
    repeat = False
    total_length = 0

    for i in range(len(string)):
        c = string[i]

        if c == '(' and not repeat:
            p_start = i + 1
            p_in = True
            continue
        if c == ')' and not repeat:
            p_end = i + 1
            p_in = False
            repeat = True
            continue
        if p_in:
            continue
        if repeat:
            cmd = string[p_start:p_end-1].split('x')
            if p_end + int(cmd[0]) - 1 <= i:
                repeat_string = string[p_end:p_end + int(cmd[0])]
                if recurive:
                    total_length += decompressedLength(repeat_string, recurive) * int(cmd[1])
                else:
                    total_length += len(repeat_string) * int(cmd[1])
                repeat = False
        else:
            total_length += 1

    return total_length

input = file('day_9.input', 'r').read().replace(' ', '')

print decompressedLength(input, False)
print decompressedLength(input, True)