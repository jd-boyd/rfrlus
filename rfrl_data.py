import datetime

from google.appengine.ext import db

import generalcounter

import ref_enc

class URL(db.Model):
 # bid        | integer                     | not null default nextval('bookmark_id_seq'::regclass)
 # url        | character varying(2048)     |
 # short_name | character varying(50)       |

 # date_added | timestamp without time zone |
 # date_used  | timestamp without time zone |
 # ip         | character varying(15)       |

    url_id = db.IntegerProperty() 
    url = db.StringProperty()
    url_key = db.StringProperty()
    short_name = db.StringProperty()
    date_added = db.DateTimeProperty()
    adding_ip = db.StringProperty()

COUNTER_NAME = "bid_cnt"

def dbAdd(remote_ip, url):
    new_id = int(generalcounter.get_count("bid_cnt"))
    generalcounter.increment("bid_cnt")

    new_key = ref_enc.encodeV(new_id)

    u = URL(
        url_id = new_id,
        url = url,
        url_key = new_key,
        #short_name = db.StringProperty()
        date_added = datetime.datetime.today(),
        adding_ip = remote_ip,
        )
    u.put()

    return new_key

def dbGet(key):
    """Key could be short_name or url_key"""

    greetings = URL.all()
    greetings.filter("url_key =", key)

    return greetings.fetch(1)[0]
