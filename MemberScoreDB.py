#  the database for all member scores

from google.appengine.ext import db

class MemberScore(db.Model):
    memberID  = db.IntegerProperty()
    score = db.IntegerProperty()