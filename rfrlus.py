from __future__ import with_statement

import os
from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db

class URLs(db.Model):
 # bid        | integer                     | not null default nextval('bookmark_id_seq'::regclass)
 # url        | character varying(2048)     |
 # short_name | character varying(50)       |

 # date_added | timestamp without time zone |
 # date_used  | timestamp without time zone |
 # ip         | character varying(15)       |

    url_id = db.IntegerProperty() 
    url = db.StringProperty()
    url_key = db.StringProperty()
    short_name = db.StringProperty()
    date_added = db.DateProperty()
    adding_ip = db.StringProperty()


class HomePage(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'

        with open(os.path.join(os.path.dirname(__file__), "main_page.html"), "r") as fh:
            self.response.out.write("".join(fh.readlines()))

class Add(webapp.RequestHandler):
    pass
        # vals = KeyVal.gql("where keyStr='count' limit 1")
        # val=None
        # for v in vals:
        #     val = v

        # if val==None:
        #     val = KeyVal()
        #     val.keyStr='count'
        #     val.ival=1

        # try:
        #     v = int(val.ival)
        # except:
        #     v=1

        # self.response.out.write("<html><body><h1>rfrl.us</h1> <p>Hello " + repr(v) + "</p></body></html>")
        # val.ival = v + 1
        # val.put()


class AddJs(webapp.RequestHandler):
    pass

class Name(webapp.RequestHandler):
    pass

class NameJs(webapp.RequestHandler):
    pass

class Ref(webapp.RequestHandler):
    pass
# Keys are the exposed methods.
#fcnDict = {'r': ref, 'add': add, 'addJs': addJs, 'altAdd': altAdd, 'createlink.php': createlink, 'name': name, 'nameJS': nameJS}


application = webapp.WSGIApplication(
                                     [('/', HomePage),
                                      ('/r', Ref),
                                      ('/add', Add),
                                      ('/addJs', AddJs),
                                      ('/name', Name),
                                      ('/nameJs', NameJs)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()


