import sys
sys.path.append("game")
from World import *

global world

while True:
    view = world.render()

    for y in range(len(view[0])):
        line = ""
        for x in range(len(view)):
            line += view[x][y].__str__()

        print(line)

    world.update()