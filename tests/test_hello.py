from webtest import TestApp

from rfrlus import application

app = TestApp(application)

def test_index():
    response = app.get('/hello')
    assert 'Hello' in str(response)

#def test_name():
#    pass

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


