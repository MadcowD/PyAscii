import sys
sys.path.append("game")
from World import *
global world

while True:
    print(world.render())
    world.input(sys.stdin.read(1))
    world.update()