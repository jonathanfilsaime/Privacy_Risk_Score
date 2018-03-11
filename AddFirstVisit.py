import webapp2
from VisitsDB import Visits

class AddFirstVisit(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        first = 0
        firstVisit = Visits(id = first)
        firstVisit.put()
