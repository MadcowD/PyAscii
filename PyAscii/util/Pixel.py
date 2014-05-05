class Pixel(object):
	def __init__(self, body, color):
		self.body = body
		self.color = color

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
