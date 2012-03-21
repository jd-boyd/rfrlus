from nose.tools import ok_, eq_

import dehttp

def test_deHTTP():
    eq_(dehttp.deHTTP("Hello%27s%21"), "Hello's!")
    eq_(dehttp.deHTTP("Phil%20Hassey%20%BB%20Blog%20Archive%20%BB%20tinypy%201.0%20-%20MIT%20License%20and%20swell%20OpenGL%20demo%20%3A%29"), 'Phil Hassey \xbb Blog Archive \xbb tinypy 1.0 - MIT License and swell OpenGL demo :)')

