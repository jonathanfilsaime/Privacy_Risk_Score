import webapp2
import json
from VisitsDB import Visits
from google.appengine.ext import db

class Admin(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Admin Page')

        visits = Visits.all().count()

        idQuery = db.GqlQuery("SELECT * FROM MemberAnswers WHERE category = " + str('authentication'))

        count = 0
        for i in idQuery:
            count += 1
        self.response.write(count)



