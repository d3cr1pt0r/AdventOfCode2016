def dragon_curve(str, size):
    b = str[::-1]
    c = ''
    for char in b:
        if char == '1':
            c += '0'
        else:
            c += '1'
    res = str + '0' + c
    if len(res) < size:
        return dragon_curve(res, size)
    return res

def get_checksum(str):
    if len(str) % 2 == 0:
        str_new = ''

        for i in xrange(0, len(str), 2):
            if str[i] == str[i+1]:
                str_new += '1'
            else:
                str_new += '0'

        return get_checksum(str_new)
    else:
        return str

input = '10011111011011001'
size = 35651584

data = dragon_curve(input, size)[:size]
checksum = get_checksum(data)

print data
print checksum