# database to keep track of the number of visitors

from google.appengine.ext import db

class Visits(db.Model):
    id = db.IntegerProperty()