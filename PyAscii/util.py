#!/usr/bin/env python

class Entity:
	def __init__(self, body, color, pos):
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
	# world = [row[:] for row in world]
	
	# global entities
	# for entity in entities:
	# 	pos = entity.pos
	# 	world[pos[1]][pos[0]] = entity.body

	world_str = "<br />".join(["".join(row) for row in world])
	return world_str