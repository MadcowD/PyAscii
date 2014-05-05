#!/usr/bin/env python

class Entity:
	def __init__(self, body, color, pos=None):
		self.body = body
		self.color = color
		self.pos = pos

	@staticmethod
	def _hex(n):
		return "{0:0{1}x}".format(n,6)

	@property
	def fg_color(self):
		return self._hex(self.color[0])

	@property
	def bg_color(self):
		return self._hex(self.color[1])

	def __str__(self):
		return self.body

ground = Entity(body="^", color=(0x33CC33, 0x663300))
world_dimensions = (50, 20)
world = [[ground] * world_dimensions[0]] * world_dimensions[1]

entities = []
player = Entity(body="@", color=(0xFF0000, 0x000000), pos=(0,0))
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
