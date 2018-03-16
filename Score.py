import webapp2
import json
from google.appengine.ext import db

class Score(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        memberID = self.request.get('id')

        score = ""
        scoreQuery = db.GqlQuery("SELECT score FROM MemberScore WHERE memberID = " + str(memberID))
        for row in scoreQuery:
            score = row.score

        jsonResponse = []
        jsonResponse.append(score)
        self.response.write(json.dumps(jsonResponse))

    def option(self):
        self.response.write("200")




