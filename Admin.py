# this class is the endpoitn for the dashboard
# it returns a Json object with the percentages
# for each of the categories
# 0-Visits (the number of people who took the survey)
# 1-Credit monitoring
# 2-Authentication
# 3-Social Media
# 4-Devices

import webapp2
import json
from VisitsDB import Visits
from ComputeCategoryPercentage import ComputeCategoryPercentage

class Admin(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Access-Control-Allow-Origin'] = '*'
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













