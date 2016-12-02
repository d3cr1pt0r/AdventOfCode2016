class KeyPad(object):

    def __init__(self):
        self.x = 1
        self.y = 1
        self.size = 3
        self.keys = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def move(self, dir):
        if dir == 'U':
            self.y -= 1
        if dir == 'D':
            self.y += 1
        if dir == 'L':
            self.x -= 1
        if dir == 'R':
            self.x += 1

        self.x = max(0, min(self.x, self.size-1))
        self.y = max(0, min(self.y, self.size-1))

    def getCurrentKey(self):
        return self.keys[self.x + self.y * self.size]


input = file('day_2.input', 'r').readlines()
keypad = KeyPad()
password = []

for line in input:
    for letter in line:
        keypad.move(letter)
    password.append(keypad.getCurrentKey())
print password