#!/usr/bin/env python

import sys
sys.path.append("game")
from Entity import Entity

ground = Entity(body="^", color=(0x33CC33, 0x663300))
world_dimensions = (50, 20)
world = [[ground] * world_dimensions[0]] * world_dimensions[1]

entities = []
player = Entity(position=(0,0), body="@", color=(0xFF0000, 0x000000))
entities.append(player)

def make_html(content):
	master_html = """
	<html>
		<head>
			<link type="text/css" rel="stylesheet" href="stylesheet.css">
		</head>
		<body>
			<div id="game">{}</div>
		</body>
	</html>
	"""
	return master_html.format(content)

def make_world_string(world):
	world = [row[:] for row in world]
	
	global entities
	for entity in entities:
		pos = entity.pos
		world[pos[1]][pos[0]] = entity

	world_str = ""
	for row in world:
		for char in row:
			world_str += "<span style=\"color: #{}; background-color: #{};\">{}</span>".format(char.fg_color, char.bg_color, char)
		world_str += "<br />"
	return world_str
