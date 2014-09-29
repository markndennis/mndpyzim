import webapp2
import cgi
import jinja2
import os
import urllib
from google.appengine.ext import ndb


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

def database_key(database_name='mnddb01'):
        """Constructs a Datastore key for a Guestbook entity with guestbook_name."""
        return ndb.Key('db', database_name)




class MainPage(webapp2.RequestHandler):
    def get(self):
        template_values = { 
            'title' : 'main',           
        }

        template = JINJA_ENVIRONMENT.get_template('/templates/templatemain.html')
        self.response.write(template.render(template_values))
        
'''
class Response(webapp2.RequestHandler):
    def post(self):
        answer = cgi.escape(self.request.get('answer'))
        
        if answer == "yes":
            snidecomment = 'yes ... she is bossy'
        else:
            snidecomment = 'no ... well sometimes she is'

        template_values = {
            'meta' :  '<meta http-equiv="refresh" content="3;/" />',
            'title' : 'response',           
            'snidecomment': snidecomment,
            'answer': answer,
        }

        template = JINJA_ENVIRONMENT.get_template('/templates/templateresult.html')
        self.response.write(template.render(template_values))
'''
        

class Greeting(ndb.Model):
    """Models an individual database entry."""
    comment = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)
   

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/response', 'response.Response'),
], debug=True)