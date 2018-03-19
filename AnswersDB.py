#  The answers database

from google.appengine.ext import db

class Answers(db.Model):
    id = db.IntegerProperty()
    answer = db.TextProperty(required = True)
    category = db.TextProperty(required = False)
    value = db.BooleanProperty()