from __future__ import with_statement

import os
import re

from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

import pystache

from rfrl_data import URL, dbAdd, dbGet
from dehttp import deHTTP
from html import *
import short

#baseUrl = "http://referurl.net/"
baseUrl = "http://opt-vm:8080/"

url_prefixs=[re.compile('^http://'), re.compile('^https://'),  re.compile('^about:'), re.compile('^ftp://')]

def matchPre(url):
    for r in url_prefixs:
        if r.match(url): return True
    return None

with open(os.path.join(os.path.dirname(__file__), "tmplt", "main_page.html"), "r") as fh:
    main_page = "".join(fh.readlines())

class HomePage(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(main_page)

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

        bid = dbAdd("", url)

        shortcutUrl = baseUrl + str(bid)

        self.response.out.write(showAltAddPage(url, shortcutUrl, warn))

with open(os.path.join(os.path.dirname(__file__), "tmplt", "add_dialog.html"), "r") as fh:
    add_dialog_tmplt = "".join(fh.readlines())


def showAltAddPage(url, shortcutUrl, warn, err="", name=""):
    aURL = short.shortenAmazonUrl(url)
    eURL = short.shortenEbayUrl(url)
    vals = {"aURL": aURL,
            "eURL": eURL,
            "baseUrl": baseUrl,
            "shortcutUrl": shortcutUrl,
            }

#    if 
#            "name": {
#            "namedShortcut": baseUrl + "r/" + name 
#            }

    return pystache.render(add_dialog_tmplt, vals)

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

        bid = dbAdd("", url)

        shortcutUrl = baseUrl + str(bid)

        self.response.out.write(showAltAddPage(url, shortcutUrl, warn))

class Name(webapp.RequestHandler):
    pass

class NameJs(webapp.RequestHandler):
    pass

class Ref(webapp.RequestHandler):
    def get(self, r):
        url = dbGet(r)
        self.response.out.write("BOB:" + url.url)

        self.redirect(url.url, permanent=True)

class Hello(webapp.RequestHandler):
    def get(self):
        self.response.out.write("Hello Bob")
        

# Keys are the exposed methods.
#fcnDict = {'r': ref, 'add': add, 'addJs': addJs, 'altAdd': altAdd, 'createlink.php': createlink, 'name': name, 'nameJS': nameJS}

url_map = [('/', HomePage),
           #('/r', Ref),
           ('/add', Add),
           ('/altAdd', AltAdd),
           ('/name', Name),
           ('/nameJs', NameJs),
           ('/hello', Hello),
           ('/([0-9A-Za-z_]+)', Ref),
           ]

def application():
    return webapp.WSGIApplication(url_map, debug=True)

def main():
    run_wsgi_app(application())

if __name__ == "__main__":
    main()


