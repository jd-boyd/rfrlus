import re

asinReStr = "[A-Z0-9]{10}"
asinRe = re.compile(asinReStr)

def shortenAmazonUrl(url_in):
    if not re.compile('^https?://(www.)?amazon.com/').match(url_in): return
    res = asinRe.search(url_in) 
    if res:
        s=res.span()
        return 'http://amzn.com/' + url_in[s[0]:s[1]]
    else:
        #Not amazon URL, or error                                               
        pass

ebayReStr = "[0-9]{12}"
ebayRe = re.compile(ebayReStr)

def shortenEbayUrl(url_in):
    if not re.compile('^https?://cgi.ebay.com/').match(url_in): return
    res = ebayRe.search(url_in)
    if res:
        s=res.span()
        return 'http://cgi.ebay.com/' + url_in[s[0]:s[1]]
    else:
        #or error in search
        pass
