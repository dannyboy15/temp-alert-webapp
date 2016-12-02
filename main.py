# Copyright 2016 Google Inc.
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

import webapp2


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')

class web_app(webapp2.RequestHandler):
    def get(self):
    	if self.request.get("foo") != '':
    		self.response.headers['Content-Type'] = 'text/plain'
        	self.response.write(self.request.get("firstName"))
        	self.response.write(self.request.get("lastName"))
        	self.response.write(self.request.get("city"))
        	self.response.write(self.request.get("state"))
        	self.response.write(self.request.get("temp"))
        	self.response.write(self.request.get("alert_time"))


        else:
        	self.response.headers['Content-Type'] = 'text/html'
        	with open('index.html', 'r') as view:	
        		self.response.write(view.read())

class web_app_s(webapp2.RequestHandler):
    def get(self, s):
    	self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(s)
    	# self.response.headers['Content-Type'] = 'text/html'
     #    with open('submit.html', 'r') as view2:	
     #    	self.response.write(view2.read())


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/webapp', web_app),
    # ('/webapp', web_app),
    
], debug=True)

