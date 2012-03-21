from nose.tools import ok_, eq_

import short

def test_amzn_good():
    eq_('http://amzn.com/B0027LSEPS', short.shortenAmazonUrl("http://www.amazon.com/gp/product/B0027LSEPS/ref=s9_simh_gw_p364_d1_i2?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=center-2&pf_rd_r=1C1SJTFCC92GW1ZX5YV4&pf_rd_t=101&pf_rd_p=470938631&pf_rd_i=507846"))
    eq_('http://amzn.com/B000A1FV62', short.shortenAmazonUrl("http://www.amazon.com/Norpro-Stainless-Steel-Spaetzle-Maker/dp/B000A1FV62/ref=pd_bbs_sr_3/104-1033474-5947108?ie=UTF8&s=home-garden&qid=1193081907&sr=8-3/akikamoza-20"))
    eq_('http://amzn.com/026256100X', short.shortenAmazonUrl("http://www.amazon.com/exec/obidos/tg/detail/-/026256100X/ref=pd_bxgy_text_1/104-2794524-3459925?v=glance&s=books&n=507846&st=*"))
    eq_('http://amzn.com/B001O7H61Y', short.shortenAmazonUrl("http://www.amazon.com/dp/B001O7H61Y/"))

def test_amzn_bad():
    ok_(not short.shortenAmazonUrl("http://bob/"))

def test_ebay_good():
    eq_('http://cgi.ebay.com/360299528689', short.shortenEbayUrl('http://cgi.ebay.com/Seagate-ST3160815AS-7200-10-160GB-SATA-Barracuda-HD-/360299528689?pt=LH_DefaultDomain_0&hash=item53e38681f1'))

    eq_('http://cgi.ebay.com/360299528689', short.shortenEbayUrl('https://cgi.ebay.com/ws/eBayISAPI.dll?ViewItem&item=360299528689'))

def test_ebay_bad():
    ok_(not short.shortenEbayUrl("http://bob/"))
    
    ok_(not short.shortenEbayUrl('http://bob/ws/eBayISAPI.dll?ViewItem&item=360299528689'))


