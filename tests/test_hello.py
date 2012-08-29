from webtest import TestApp

from rfrlus import application

app = TestApp(application)

def test_index():
    response = app.get('/hello')
    assert 'Hello' in str(response)
