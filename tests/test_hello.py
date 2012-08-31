from webtest import TestApp

from rfrlus import application

app = TestApp(application)

def test_add_blank():
    try:
        resp = app.post('/add', {'url': ''})
    except Exception:
        pass
    else:
        assert False, "Blank URLs shouldn't be accepted."

def test_add():
    resp = app.post('/add', {'r': 'http://bobsays.com'})
    
    print resp

    assert "Your shortcut is: " in resp.unicode_body
    assert '/6">http://' in resp.unicode_body


def test_ref():
    resp = app.post('/add', {'r': 'http://bobsays.com'})
    
    #should be /6

    resp = app.get('/6', status=301)
    print resp.headers['Location']
    assert resp.headers['Location'] == 'http://bobsays.com'

def test_ref_fail():
    resp = app.post('/add', {'r': 'http://bobsays.com'})
    
    resp = app.get('/7', status=404)

    

#def test_name():
#    pass
