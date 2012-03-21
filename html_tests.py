from nose.tools import ok_, eq_

import html

def test():
    h = html.HDoc()

    h.addHead(html.title("Bob Page"))
    h.addScript("referurl_dialog.js")

    h.add(html.h1("Test page"))
    h.add(html.p("Is this working now?"))

    eq_("".join(h), '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html;charset=utf-8" /><title>Bob Page</title>\n<script type="text/javascript" src="referurl_dialog.js"></script>\n</head>\n<body><h1>Test page</h1>\n<p>Is this working now?</p>\n</body></html>')
