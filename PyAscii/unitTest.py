import sys
sys.path.append("game")
from World import *

global world

while True:
    view = world.render()

    for y in range(world.size.y):
        line = ""
        for x in range(world.size.x):
            line += view[x][y].__str__()

        print(line)

    world.input(sys.stdin.read(1))
    world.update()