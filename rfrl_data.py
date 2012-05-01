import datetime

from google.appengine.ext import db

import generalcounter

import ref_enc

# From:
# http://squeeville.com/2009/01/30/add-a-unique-constraint-to-google-app-engine/
class Unique(db.Model):
    @classmethod
    def check(cls, scope, value):
        def tx(scope, value):
            key_name = "U%s:%s" % (scope, value,)
            print "KN:", key_name
            ue = Unique.get_by_key_name(key_name)
            if ue:
                raise UniqueConstraintViolation(scope, value)
            ue = Unique(key_name=key_name)
            ue.put()
        db.run_in_transaction(tx, scope, value)


class UniqueConstraintViolation(Exception):
    def __init__(self, scope, value):
        super(UniqueConstraintViolation, self).__init__("Value '%s' is not unique within scope '%s'." % (value, scope, ))

class URL(db.Model):
 # bid        | integer                     | not null default nextval('bookmark_id_seq'::regclass)
 # url        | character varying(2048)     |
 # short_name | character varying(50)       |

 # date_added | timestamp without time zone |
 # date_used  | timestamp without time zone |
 # ip         | character varying(15)       |

    #url_id = db.IntegerProperty() 
    url = db.LinkProperty(required=True)
    url_key = db.StringProperty(required=True)
    short_name = db.StringProperty()
#    date_added = db.DateTimeProperty()
#    adding_ip = db.StringProperty()

    @classmethod
    def create(cls, url, url_key):
        Unique.check("urlkey", url_key)
        a = URL(url=url, url_key=url_key)
        a.put()
        return a

COUNTER_NAME = "bid_cnt"

def newId():
    new_id = int(generalcounter.get_count(COUNTER_NAME))
    generalcounter.increment(COUNTER_NAME)
    return new_id

def dbInject(url, url_key, short_name=""):
    u = URL.create(
        url = url,
        url_key = url_key,
        )
    u.short_name = short_name
    u.put()
    return u

def dbAdd(url):
    new_id = int(generalcounter.get_count(COUNTER_NAME))
    generalcounter.increment(COUNTER_NAME)

    new_key = ref_enc.encodeV(new_id)

    u = URL.create(
        #url_id = new_id,
        url = url,
        url_key = new_key,
        #short_name = db.StringProperty()
#        date_added = datetime.datetime.today(),
#        adding_ip = remote_ip,
        )
    #u.put()

    return new_key

def dbGet(key):
    """Key could be short_name or url_key"""

    urls = URL.all()
    urls.filter("url_key =", key)

    return urls.fetch(1)[0]


def dbName(key, name):
    pass
