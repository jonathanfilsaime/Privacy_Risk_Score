# this class is the API endpoint for the
# survey page. It returns 2 JSON object
# JSON 1 - [id, question, category ]
# JSON 2 - [id, answer ]

import webapp2
import json
from QuestionsDB import Questions
from AnswersDB import Answers
from ScoreCalculator import ScoreCalculator
from VisitsDB import Visits

class Survey(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        questionsDictionary = []
        questions = Questions.all()
        questions.order('id')

        for question in questions:

            questionDic = {
                'id' : question.id,
                'question' : question.question,
                'category' : question.category
            }
            questionsDictionary.append(questionDic)

        answersDictionary = []
        answers = Answers.all()
        answers.order('id')

        for answer in answers:
            answerDic = {
                'id' : answer.id,
                'answer' : answer.answer,
                'value' : answer.value
            }
            answersDictionary.append(answerDic)

        jsonResponse = []
        jsonResponse.append(questionsDictionary)
        jsonResponse.append(answersDictionary)
        self.response.write(json.dumps(jsonResponse))

    def post(self):
        responses = json.loads(self.request.body)

        responseArray = []
        for key in responses:
            for value in key:
                responseArray.append(key[value].rstrip())

        visits = Visits.all().count()
        memberID = visits + 1
        visitor = Visits(id = memberID)
        visitor.put()

        compute = ScoreCalculator()
        score = compute.computeScore(responseArray, memberID)

        jsonResponse = []
        jsonResponse.append(score)
        self.response.write(json.dumps(jsonResponse))












