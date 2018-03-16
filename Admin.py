import webapp2
import json
from VisitsDB import Visits
from ComputeCategoryPercentage import ComputeCategoryPercentage

class Admin(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'

        visits = Visits.all().count()
        percentage = ComputeCategoryPercentage()
        credit = percentage.compute("credit monitoring")
        authentication = percentage.compute("authentication")
        social = percentage.compute("social media")
        devices = percentage.compute("devices")

        dashboard = {
            'visits' : visits,
            'credit monitoring' : credit,
            'authentication' : authentication,
            'social media' : social,
            'devices' : devices
        }

        jsonResponse = []
        jsonResponse.append(dashboard)
        self.response.write(json.dumps(jsonResponse))













