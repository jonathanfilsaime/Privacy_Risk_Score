#  the database for all member answers

from google.appengine.ext import db

class MemberAnswers(db.Model):
    memberID  = db.IntegerProperty()
    questionID = db.IntegerProperty()
    answer = db.TextProperty(required = True)
    category = db.StringProperty(required = True)
    value = db.BooleanProperty()