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

class WtfKeyPad(object):

    def __init__(self):
        self.x = 0
        self.y = 2
        self.denied_indexes = [0, 1, 3, 4, 5, 9, 15, 19, 20, 21, 23, 24]
        self.size = 5
        self.keys = ['0', '0', '1', '0', '0',
                     '0', '2', '3', '4', '0',
                     '5', '6', '7', '8', '9',
                     '0', 'A', 'B', 'C', '0',
                     '0', '0', 'D', '0', '0'
        ]

    def move(self, dir):
        if dir == 'U':
            self.y -= 1
            if self.isDeniedPosition(self.x, self.y):
                self.y += 1
        if dir == 'D':
            self.y += 1
            if self.isDeniedPosition(self.x, self.y):
                self.y -= 1
        if dir == 'L':
            self.x -= 1
            if self.isDeniedPosition(self.x, self.y):
                self.x += 1
        if dir == 'R':
            self.x += 1
            if self.isDeniedPosition(self.x, self.y):
                self.x -= 1

        self.x = max(0, min(self.x, self.size-1))
        self.y = max(0, min(self.y, self.size-1))

    def isDeniedPosition(self, x, y):
        return (x + y * self.size) in self.denied_indexes

    def getCurrentKey(self):
        return self.keys[self.x + self.y * self.size]


input = file('day_2.input', 'r').readlines()
keypad = KeyPad()
wtfKeypad = WtfKeyPad()
password1 = []
password2 = []

for line in input:
    for letter in line:
        keypad.move(letter)
        wtfKeypad.move(letter)
    password1.append(keypad.getCurrentKey())
    password2.append(wtfKeypad.getCurrentKey())

print password1
print password2