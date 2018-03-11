from google.appengine.ext import db

class Answers(db.Model):
    id = db.IntegerProperty()
    answer = db.TextProperty(required = True)
    value = db.BooleanProperty()