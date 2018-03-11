import webapp2
from VisitsDB import Visits

class Visits(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        visits = Visits.all()
        visits.order('memberID')

        for vs in visits:
            self.response.write(vs)