import webapp2
import json
from MemberScoreDB import MemberScore

class Score(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'

    def post(self):
        self.response.headers['Access-Control-Allow-Origin'] = '*'
        self.response.headers['Content-Type'] = 'text/plain'
        memberID = json.loads(self.request.body)

        member = ""
        for i in memberID:
            member = i

        score = ""
        memberScores = MemberScore.all()
        for memberScore in memberScores:
            if memberScore.memberID == member:
                score = memberScore.score

        jsonResponse = []
        jsonResponse.append(score)
        self.response.write(json.dumps(jsonResponse))

    def options(self):
        self.response.headers['Access-Control-Allow-Origin'] = '*'
        self.response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        self.response.headers['Allow'] = 'GET, POST'
        self.response.write("200 OK")




