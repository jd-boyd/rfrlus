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

if __name__=='__main__':
    import unittest

    class TestAmazon(unittest.TestCase):
        def test_good(self):
            self.assertEqual('http://amzn.com/B0027LSEPS', shortenAmazonUrl("http://www.amazon.com/gp/product/B0027LSEPS/ref=s9_simh_gw_p364_d1_i2?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=center-2&pf_rd_r=1C1SJTFCC92GW1ZX5YV4&pf_rd_t=101&pf_rd_p=470938631&pf_rd_i=507846"))
            self.assertEqual('http://amzn.com/B000A1FV62', shortenAmazonUrl("http://www.amazon.com/Norpro-Stainless-Steel-Spaetzle-Maker/dp/B000A1FV62/ref=pd_bbs_sr_3/104-1033474-5947108?ie=UTF8&s=home-garden&qid=1193081907&sr=8-3/akikamoza-20"))
            self.assertEqual('http://amzn.com/026256100X', shortenAmazonUrl("http://www.amazon.com/exec/obidos/tg/detail/-/026256100X/ref=pd_bxgy_text_1/104-2794524-3459925?v=glance&s=books&n=507846&st=*"))
            self.assertEqual('http://amzn.com/B001O7H61Y', shortenAmazonUrl("http://www.amazon.com/dp/B001O7H61Y/"))

        def test_bad(self):
            self.assertFalse(shortenAmazonUrl("http://bob/"))


    class TestEbay(unittest.TestCase):
        def test_good(self):
            self.assertEqual('http://cgi.ebay.com/360299528689', shortenEbayUrl('http://cgi.ebay.com/Seagate-ST3160815AS-7200-10-160GB-SATA-Barracuda-HD-/360299528689?pt=LH_DefaultDomain_0&hash=item53e38681f1'))

            self.assertEqual('http://cgi.ebay.com/360299528689', shortenEbayUrl('https://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=360299528689'))

        def test_bad(self):
            self.assertFalse(shortenEbayUrl("http://bob/"))

            self.assertFalse(shortenEbayUrl('http://bob/ws/eBayISAPI.dll?ViewItem&item=360299528689'))

    unittest.main()
