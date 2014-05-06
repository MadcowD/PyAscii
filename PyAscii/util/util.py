#!/usr/bin/env python

import sys
sys.path.append("game")
from World import *

def make_html(content):
    master_html = """
    <html>
        <head>
            <link type="text/css" rel="stylesheet" href="stylesheet.css">
            <script type="text/css" src="keyboard"></script>
        </head>
        <body>
            <div id="game">{}</div>
            Player @ ({},{})
        </body>
    </html>
    """
    return master_html.format(content, world.player.pos.x, world.player.pos.y)

def make_world_string(world):
    world_str = ""
    for y in range(len(world[0])):
        for x in range(len(world)):
            world_str += "<span style=\"color: #{}; background-color: #{};\">{}</span>"\
                .format(world[x][y].fg_color, world[x][y].bg_color, world[x][y])
        world_str += "<br />"
    return world_str
