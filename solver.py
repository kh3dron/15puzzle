from scramble import (ImageScrambleGame, MOVE_UP,MOVE_LEFT,MOVE_DOWN,MOVE_RIGHT)
import copy

g = ImageScrambleGame(gsize=3)
print("\nStart state: ", g.get_state(), "\n")

#node class to help bundle some things together for the A* search methods
class node():
        def __init__(self, g=None, history=[]):
                self.g = g
                self.history = history
                self.distOut = len(history)
                self.hDist = h_dist(g)
                self.totalDist = self.distOut + self.hDist
        def update(self):
                self.distOut = len(self.history)
                self.hDist = h_dist(g)
                self.totalDist = self.distOut + h_dist(self.g)

# state to a line: should review list comprehensions
def state_to_line(state):
        res = []
        for a in state:
                for b in a:
                        res.append(b)
        return res

#A* Heuristic: distance from any board state to the solved state
# Sum of Manhattan distances of each tile to its solved position
def h_dist(g):
        manhattanDist = 0
        t = (g.get_state())
        t = state_to_line(t)
        for c, tile in enumerate(t):
                if tile == -1:
                        continue
                placedX, placedY = ((c) // g.gsize), ((c) % g.gsize)
                desiredX, desiredY = ((tile) // g.gsize), ((tile) % g.gsize)
                delt = abs(desiredX - placedX) + abs(desiredY - placedY)
                manhattanDist += delt
        return manhattanDist

#get what moves are possible depending on where the empty spot is
def legal_moves(g):
        goods = []
        p = g.whitespot_idx
        if (p % g.gsize) != 0: goods.append(1)          #can move left
        if p > g.gsize-1: goods.append(0)               #can move up
        if ((p+1) % g.gsize) != 0: goods.append(3)      #can move right
        if p < (g.gsize*(g.gsize-1))-1: goods.append(2) #can move down
        return goods

#dumb queue insertion
#should definitely make this better for runtime's sake
def inPoint(e, q):
        for c,g in enumerate(q):
                if g.totalDist > e.totalDist:
                        return c
        return -1

#main A*
#A set prevents us from re-evaulating already seen states, such as making then un-making the same move
def solve(g):

        start = node(g)
        queue = [start]
        seen = set()
        seen.add(hash(str(start.g.get_state()))) 

        t = 1
        while queue:
                if t % 1000 == 0:
                        print("tested", t, "solutions")
                cur = queue[0]
                queue.remove(cur)
                dist = h_dist(cur.g)
                if dist == 0:
                        #print("Solution found!")
                        print("\n", cur.history)
                        return
                steps = legal_moves(cur.g)
                for s in steps:
                        new = copy.deepcopy(cur)
                        new.g = copy.deepcopy(cur.g) #this might be overkill but it definitely works this way 
                        new.g.move_blank(s)
                        new.update()
                        if hash(str(new.g.get_state())) not in seen:
                                new.history.append(s)
                                queue.insert(inPoint(new, queue), new)
                                t += 1
                                seen.add(hash(str(new.g.get_state()))) 
