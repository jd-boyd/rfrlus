from __future__ import with_statement

import os
from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from rfrl_data import URL, dbAdd, dbGet

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

def showAltAddPage(url, shortcutUrl, u, warn, err="", name=""):
    h=HDoc()
    h.addHead('<link rel="stylesheet" type="text/css" href="style_iframe.css" title="default"/>')
    h.addHead("""
<script type='text/javascript'>
  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-18857050-3']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type =
    'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' :
    'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0];
    s.parentNode.insertBefore(ga, s);
  })();
</script>""")
    h.addHead(title('ReferURL: Add'))
    h.addScript('name.js')
    h.addScript('ajax.js')
    
    h.add(h1("ReferURL"))

    aURL = short.shortenAmazonUrl(url)
    if aURL:
        h.add(p("I noticed that the URL you are shortening is from Amazon.  Perhaps would would prefer a shorter Amazon URL to use:" + br() +ahref(aURL,aURL)))

    eURL = short.shortenEbayUrl(url)
    if eURL:
        h.add(p("I noticed that the URL you are shortening is from eBay.  Perhaps would would prefer a shorter eBay URL to use:" + br() +ahref(eURL,eURL)))

    h.add(p("Your shortcut is:" + ahref(shortcutUrl,shortcutUrl)))

    h.add(h2('Mail it!'))
    h.add(p("Click " + ahref('mailto:?body=' +shortcutUrl ,'here') + ' to open a message in your local mail program.'))

    h.add(h2('Customize?'))
    h.add(p("You are limited to a maximum of 20 characters.<br>  Special characters will be replaced with URL safe replacement characters."))
    h.add('<div id="custom">')

    h.add('<div id="errField"></div>')

    if err=="" and not name=="":
        namedShortcut = baseUrl + "r/" + name
        h.add(p(ahref(namedShortcut,namedShortcut)))
    else:

        h.add('<form method="post" action="name" onsubmit="setName(); return false;" id="nameForm">')
        if not err=="":
            h.add(p(err))
        h.add('<input type="hidden" name="u" value="' + u + '">\n')
        h.add(baseUrl + 'r/<input type="text" name="n" value='+repr(name)+'><input type="submit" value="Name" />')
        h.add('</form>')
    h.add('</div>')

    h.add(hr())
    h.add(p("This service is brought to you by " + ahref('http://jdboyd.net/','JDBoyd.net') + '.'))
    return h.output()


class AltAdd(webapp.RequestHandler):
    def get(self):
        warn=False
        url = deHTTP(r)

        #Check if url matches one of url_prefixes.  If not, pre-pend http://
        if not matchPre(url): 
            url = "http://" + url
            warn=True

        #string with IP in it.
        #I should log to DB
        #along with useragent
        u=str(uuid.uuid4())

        bid = dbAdd(req, url, u)

        shortcutUrl = baseUrl + str(bid)
        #shortcutUrl = baseUrl + ref_enc.encodeV(bid)

        self.response.out.write(showAltAddPage(url, shortcutUrl, u, warn))

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
                                      ('/altAdd', AltAdd),
                                      ('/name', Name),
                                      ('/nameJs', NameJs)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()


