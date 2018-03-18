from google.appengine.ext import db

class Recommendations(db.Model):
    recommendation = db.TextProperty(required = True)
    link = db.TextProperty(required=True)
    category = db.TextProperty(required = True)
