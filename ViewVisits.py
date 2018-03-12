import webapp2
from VisitsDB import Visits

class ViewVisits(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        visits = Visits.all().count()

        self.response.write(visits)