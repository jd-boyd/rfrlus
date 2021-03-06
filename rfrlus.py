from __future__ import with_statement

import os
import re

from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

import jinja2

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'tmplt')))

from rfrl_data import URL, dbAdd, dbGet
from dehttp import deHTTP
from html import *
import short

#baseUrl = "http://rfrl.us/"
baseUrl = "http://192.168.56.101:8080/"

url_prefixs=[re.compile('^http://'), re.compile('^https://'),  re.compile('^about:'), re.compile('^ftp://')]

def matchPre(url):
    for r in url_prefixs:
        if r.match(url): return True
    return None

class HomePage(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(jinja_environment.get_template("main_page.html").render())

class Add(webapp.RequestHandler):
    def post(self):
        self.get()

    def get(self):
        warn=False
        url = deHTTP(self.request.get('r'))

        #Check if url matches one of url_prefixes.  If not, pre-pend http://
        if not matchPre(url): 
            url = "http://" + url
            warn=True

        bid = dbAdd(url)

        shortcutUrl = baseUrl + str(bid)

        self.response.out.write(showAltAddPage(url, shortcutUrl, warn))

def showAltAddPage(url, shortcutUrl, warn, err="", name=""):
    aURL = short.shortenAmazonUrl(url)
    eURL = short.shortenEbayUrl(url)
    vals = {"aURL": aURL,
            "eURL": eURL,
            "baseUrl": baseUrl,
            "shortcutUrl": shortcutUrl,
            }

    return jinja_environment.get_template("add_dialog.html").render(vals)

class AltAdd(webapp.RequestHandler):
    def POST(self):
        self.GET()

    def get(self):
        warn=False
        url = deHTTP(self.request.get('r'))

        #Check if url matches one of url_prefixes.  If not, pre-pend http://
        if not matchPre(url): 
            url = "http://" + url
            warn=True

        #string with IP in it.
        #I should log to DB
        #along with useragent
        #u=str(uuid.uuid4())

        bid = dbAdd(url)

        shortcutUrl = baseUrl + str(bid)

        self.response.out.write(showAltAddPage(url, shortcutUrl, warn))

class Name(webapp.RequestHandler):
    def POST(self):
        self.GET()

    def get(self):
        u = self.request.get('u')
        n = self.request.get('n')

        self.response.out.write(showAltAddPage(u, 
                                               shortcutUrl, warn, 
                                               name=n))
class NameJs(webapp.RequestHandler):
    def POST(self):
        self.GET()

    def get(self):
        self.response.headers['Content-Type'] = 'application/json'

        u = self.request.get('u')
        n = self.request.get('n')

        rd={'result': None, 'id': 0, 'error': None} #Response dictionary

        self.response.out.write(json.dumps(rd))


class Ref(webapp.RequestHandler):
    def get(self, r):
        try:
            url = dbGet(r)
        except IndexError:
            print "SR:", dir(self.response)
            self.response.set_status( 404 )

        #self.response.out.write("BOB:" + url.url)

        #self.redirect(url.url, permanent=True)

# Keys are the exposed methods.
#fcnDict = {'r': ref, 'add': add, 'addJs': addJs, 'altAdd': altAdd, 'createlink.php': createlink, 'name': name, 'nameJS': nameJS}

url_map = [('/', HomePage),
           #('/r', Ref),
           ('/add', Add),
           ('/altAdd', AltAdd),
           ('/name', Name),
           ('/nameJs', NameJs),
           ('/([0-9A-Za-z_]+)', Ref),
           ]

application = webapp.WSGIApplication(url_map, debug=True)

