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
import sys
import time
sys.path.append("util")
from util import *
sys.path.pop()
sys.path.append("game")
from World import *


class WorldHandler(webapp2.RequestHandler):
    def get(self):
        global world

        world.input(self.request.get('input'))
        world.update()
        view = world.render()

        self.response.write(make_html(make_world_string(view)))

    def post(self):
        global world

        #send json requests to /world 
        #post your input in a post variable called inpiut


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("This should serve the main page")

app = webapp2.WSGIApplication([
    ('/world', WorldHandler),
    ('/', MainHandler),
], debug=True)
