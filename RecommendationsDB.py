# this database holds all the recommendation

from google.appengine.ext import db

class Recommendations(db.Model):
    link = db.TextProperty(required=True)
    category = db.TextProperty(required = True)
