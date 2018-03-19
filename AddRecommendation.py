# this class read from a file and populates the
# database table RecommendationsDB
# this is strictly for admin use

import webapp2
import io
from RecommendationsDB import Recommendations

class AddRecommendation(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.storeInRecommendationsDB("recommendations.txt")
        self.response.write("recommendations have been added")

    def storeInRecommendationsDB(self, fileNameAndPath):
        with io.open(fileNameAndPath) as file:
            for line in file:
                element = line.split(',')

                self.response.write(element[0])
                self.response.write(element[1])
                recommendation = Recommendations(link = element[0], category = element[1])
                recommendation.put()
