from google.appengine.ext import db

class Questions(db.Model):
    id = db.IntegerProperty()
    question = db.StringProperty(required = True)
    category = db.StringProperty(required = True)