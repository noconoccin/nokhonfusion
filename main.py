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
import os
import jinja2
import webapp2
import logging

JINJA_ENVIRONMENT = jinja2.Environment(
	loader = jinja2.FileSystemLoader(os.path.dirname(__file__) + "/templates"))

class MainPage(webapp2.RequestHandler):
    def get(self):
        fctext = self.request.get('fctext')
        logging.info(fctext)
        translation = "[Test] This is the translation."
        template_vars = {
          'translation': translation
        }
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.out.write(template.render(template_vars))
		
class Translate(webapp2.RequestHandler):
    def post(self):
        fctext = self.request.get('fctext')
        logging.info(fctext)
        translation = "[Test] This is the translation 2."
        template_vars = {
          'translation': translation
        }
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.out.write(template.render(template_vars))


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/translate', Translate)
], debug=True)
