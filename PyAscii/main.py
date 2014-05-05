#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import time

class Entity:
	def __init__(self, body, color):
		self.body = body
		self.color = color

	@property
	def fg_color(self):
		return self.color[0]

	@property
	def bg_color(self):
		return self.color[1]

ground = Entity(body="^", color=(0x3C3, 0x630))
world_dimensions = (20,20)
world = [[ground.body] * world_dimensions[0]] * world_dimensions[1]

class MainHandler(webapp2.RequestHandler):
    def get(self):
    	i = 1
    	while True:
    		time.sleep(0.5)
        	self.response.write(i)
        	i += 1

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
