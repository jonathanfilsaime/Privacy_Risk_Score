# this class computes the score and the averages

import webapp2
import json
from MemberScoreDB import MemberScore
from RecommendationEngine import RecommendationEngine

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

        count = 0
        totalScore =  0
        score = 0

        memberScores = MemberScore.all()
        for memberScore in memberScores:
            count += 1
            totalScore += int(memberScore.score)

            if memberScore.memberID == member:
                score = memberScore.score

        average = totalScore / count

        scoreObject = []
        scoreDic = {
            'total' : 100,
            'score' : score,
            'average' : average,
        }
        scoreObject.append(scoreDic)

        recommendation = RecommendationEngine()
        recommendationObject = recommendation.recommend(member)

        jsonResponse = []
        jsonResponse.append(scoreObject)
        jsonResponse.append(recommendationObject)
        self.response.write(json.dumps(jsonResponse))

    def options(self):
        self.response.headers['Access-Control-Allow-Origin'] = '*'
        self.response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        self.response.headers['Allow'] = 'GET, POST'
        self.response.write("200 OK")




