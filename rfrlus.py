import os
from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db

class KeyVal(db.Model):
    keyStr = db.StringProperty()
    sval = db.StringProperty() 
    ival = db.IntegerProperty() 

class MainPage(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            self.response.headers['Content-Type'] = 'text/html'

            vals = KeyVal.gql("where keyStr='count' limit 1")
            val=None
            for v in vals:
                val = v

            if val==None:
                val = KeyVal()
                val.keyStr='count'
                val.ival=repr(1)

            try:
                v = int(val.ival)
            except:
                v=1

            self.response.out.write("<html><body><h1>rfrl.us</h1> <p>Hello " + user.nickname() + " " + repr(v) + "</p></body></html>")
            val.ival = v+ 1
            val.put()
        else:
            self.redirect(users.create_login_url(self.request.uri))

application = webapp.WSGIApplication(
                                     [('/', MainPage)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()


