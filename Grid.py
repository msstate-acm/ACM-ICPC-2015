class Node:
    def __init__(self, distance):
        self.distance = int(distance)
        self.neighbors = []
        self.position = None
        self.parent = None
    
    def add(self, other):
        self.neighbors.append(other)
        
    def addToQ(self, Q):
        for n in self.neighbors:
            if n not in Q and n != self.parent:
                n.parent = self
                Q.append(n)
        
    def __repr__(self):
        return str(self.distance) + str(self.position)
        
        
def BFS(Q):
    while Q:
        e = Q.pop(0)
        if e.position == goalPosition:
            return e
        e.addToQ(Q)
    return -1


h, w = list(map(int, input().split()))

grid = []
for _ in range(h):
    grid.append(list(map(Node, input())))

for row in range(h):
    for col in range(w):
        n = grid[row][col]
        n.position = (row,col)
        if n.distance == 0:
            continue
        
        if row - n.distance >= 0:
            n.add(grid[row - n.distance][col])
        if row + n.distance < h:
            n.add(grid[row + n.distance][col])
        if col + n.distance < w:
            n.add(grid[row][col + n.distance])
        if col - n.distance >= 0:
            n.add(grid[row][col - n.distance])
            
root = grid[0][0]
goalPosition = (h-1, w-1)
Q = []
root.addToQ(Q)
goal = BFS(Q)
if goal == -1:
    print(-1)
    exit()

parent = goal.parent
pathLength = 0
while parent is not None:
    pathLength += 1
    parent = parent.parent
print(pathLength)
