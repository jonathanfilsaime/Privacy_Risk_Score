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
                self.response.write(element[2])
                recommendation = Recommendations(recommendation = element[0], link = element[1], category = element[2])
                recommendation.put()
