import re
from PIL import Image

input = file('day_8.input', 'r').readlines()

class ChinaDisplay(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = None

        self.initPixelMatrix(self.width, self.height)

    def initPixelMatrix(self, width, height):
        self.pixels = [[0 for y in range(height)] for x in range(width)]

    def isInBounds(self, x=0, y=0):
        return x >= 0 and x < self.width and y >= 0 and y < self.height

    def fillAxB(self, x, y):
        if not self.isInBounds(x, y):
            return

        for y_1 in range(y):
            for x_1 in range(x):
                self.pixels[x_1][y_1] = 1

    def shiftRight(self, y, n):
        if not self.isInBounds(0, y):
            return

        copy = []
        a = n % self.width
        for x_1 in range(self.width):
            copy.append(self.pixels[x_1][y])
        copy = copy[-a:] + copy[:-a]

        for x_1 in range(self.width):
            self.pixels[x_1][y] = copy[x_1]

    def shiftDown(self, x, n):
        if not self.isInBounds(x, 0):
            return

        a = n % self.height
        self.pixels[x] = self.pixels[x][-a:] + self.pixels[x][:-a]

    def getLitPixels(self):
        total_pixels = 0
        for y in range(self.height):
            for x in range(self.width):
                if self.pixels[x][y] == 1:
                    total_pixels += 1
        return total_pixels

    def getImage(self):
        im = Image.new('1', (self.width, self.height), 'black')
        pix = im.load()
        for y in range(self.height):
            for x in range(self.width):
                pix[x, y] = self.pixels[x][y]
        return im

    def printMatrix(self):
        for y in range(self.height):
            row = ''
            for x in range(self.width):
                row += str(self.pixels[x][y])
            print row

display = ChinaDisplay(50, 6)

for line in input:
    line = line.strip()

    if 'rect' in line:
        r = re.match(r'rect ([0-9]*)x([0-9]*)', line)
        x = int(r.group(1))
        y = int(r.group(2))

        display.fillAxB(x, y)
    if 'rotate row' in line:
        r = re.match(r'rotate row y=([0-9]*) by ([0-9]*)', line)
        y = int(r.group(1))
        n = int(r.group(2))

        display.shiftRight(y, n)
    if 'rotate column' in line:
        r = re.match(r'rotate column x=([0-9]*) by ([0-9]*)', line)
        x = int(r.group(1))
        n = int(r.group(2))

        display.shiftDown(x, n)

print display.getLitPixels()
display.getImage().show()