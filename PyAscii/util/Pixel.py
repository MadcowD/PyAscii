class Pixel(object):
	def __init__(self, body, color):
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