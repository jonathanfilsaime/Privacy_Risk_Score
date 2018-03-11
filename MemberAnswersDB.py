from google.appengine.ext import db

class MemberAnswers(db.Model):
    memberID  = db.IntegerProperty()
    questionID = db.IntegerProperty()
    answer = db.TextProperty(required = True)
    value = db.BooleanProperty()