import datetime

from nose.tools import ok_, eq_, with_setup
import unittest

import rfrl_data

from google.appengine.ext import testbed

def setUp():
    from google.appengine.api import apiproxy_stub_map
    from google.appengine.api import datastore_file_stub
    
            # Use a fresh stub datastore.
    apiproxy_stub_map.apiproxy = apiproxy_stub_map.APIProxyStubMap()
    stub = datastore_file_stub.DatastoreFileStub('appid', '/dev/null',
                                                 '/dev/null')
    apiproxy_stub_map.apiproxy.RegisterStub('datastore_v3', stub)
    
    tb = testbed.Testbed()
    # Then activate the testbed, which prepares the service stubs for use.
    tb.activate()
    # Next, declare which service stubs you want to use.
    tb.init_datastore_v3_stub()
    tb.init_memcache_stub()
    #tb.deactivate()
        
def tearDown():
    pass

def test_url():
    u = rfrl_data.URL(
        url_id = 1,
        url = "url",
        url_key = "d",
        #short_name = db.StringProperty()
        date_added = datetime.datetime.today(),
        adding_ip = "",
        )
    k = u.put()
    print "K", k

    urls = rfrl_data.URL.all()
    urls.filter("url_key =", "d")

    eq_(urls.fetch(1)[0].url, "url")

@with_setup(setUp, tearDown)
def test_newid():
    eq_(rfrl_data.newId(), 0)

@with_setup(setUp, tearDown)
def test_newid2():
    eq_(rfrl_data.newId(), 0)

@with_setup(setUp, tearDown)
def test_add():
    rfrl_data.newId() # First new ID on a clear datastore is ''

    eq_(rfrl_data.dbAdd("", "http://something"), '6')

    eq_(rfrl_data.dbGet('6').url, "http://something")
    


