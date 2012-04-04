from nose.tools import ok_, eq_
from nose.exc import SkipTest

import ref_enc

def test_2546():
    z = 2546
    print "start", z
    t = ref_enc.encodeV(z)
    print repr(t)

    eq_(z, ref_enc.decodeV(t))
    
def test_10_mil():
    z = 10000000
    print "start", z
    t = ref_enc.encodeV(z)

    eq_(z, ref_enc.decodeV(t))

def test_range():    
    for i in range(10000):
        t = ref_enc.encodeV(i)
        eq_(i,ref_enc.decodeV(t))

