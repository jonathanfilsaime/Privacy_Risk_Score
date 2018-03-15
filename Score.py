import webapp2
import json
from google.appengine.ext import db

class Score(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        response = self.request.GET
        self.response.write(response)

        # for r in response:
        #     self.response.write(r)


        memberID = ""
        idQuery = db.GqlQuery("SELECT id FROM Visits ORDER BY id DESC LIMIT 1")
        for row in idQuery:
            memberID = row.id

        score = ""
        scoreQuery = db.GqlQuery("SELECT score FROM MemberScore WHERE memberID = " + str(memberID))
        for row in scoreQuery:
            score = row.score

        jsonResponse = []
        jsonResponse.append(score)
        self.response.write(json.dumps(jsonResponse))

    def option(self):
        self.response.write("200")




