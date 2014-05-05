#!/usr/bin/env python

class Entity:
	def __init__(self, body, color, pos=None):
		self.body = body
		self.color = color
		self.pos = pos

	@property
	def fg_color(self):
		return self.color[0]

	@property
	def bg_color(self):
		try:
			return self.color[1]
		except:
			return 0xFFF

ground = Entity(body="^", color=(0x3C3, 0x630))
world_dimensions = (50, 20)
world = [[ground.body] * world_dimensions[0]] * world_dimensions[1]

entities = []
player = Entity(body="@", color=(0xF00, 0x000), pos=(0,0))
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
		world[pos[1]][pos[0]] = entity.body

	world_str = "<br />".join(["".join(row) for row in world])
	return world_str