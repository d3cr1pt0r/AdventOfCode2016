import Queue

class Node(object):

    def __init__(self, x, y, distance):
        self.x = x
        self.y = y
        self.distance = distance

    def isWall(self, x, y):
        return (len('{0:b}'.format((x*x + 3*x + 2*x*y + y + y*y) + 1362).replace('0', '')) % 2) != 0

    def possibleNeighbours(self):
        possible_nodes = []

        if not self.isWall(self.x + 1, self.y):
            possible_nodes.append((self.x + 1, self.y))
        if self.x - 1 >= 0 and not self.isWall(self.x - 1, self.y):
            possible_nodes.append((self.x - 1, self.y))
        if not self.isWall(self.x, self.y + 1):
            possible_nodes.append((self.x, self.y + 1))
        if self.y - 1 >= 0 and not self.isWall(self.x, self.y - 1):
            possible_nodes.append((self.x, self.y - 1))

        return possible_nodes

root = Node(1, 1, 0)
visited_nodes = set()
queue = [root]
s_1 = False
s_2 = False

while len(queue) > 0:
    node = queue.pop(0)

    if not s_1:
        if node.x == 31 and node.y == 39:
            print node.distance
            s_1 = True

    if not s_2:
        if node.distance > 50:
            print len(visited_nodes)
            s_2 = True


    visited_nodes.add((node.x, node.y))

    possible_neighbours = node.possibleNeighbours()
    for n in possible_neighbours:
        if n not in visited_nodes:
            queue.append(Node(n[0], n[1], node.distance + 1))
