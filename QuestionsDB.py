#  The database for al questions

from google.appengine.ext import db

class Questions(db.Model):
    id = db.IntegerProperty()
    question = db.TextProperty(required = True)
    category = db.TextProperty(required = False)
