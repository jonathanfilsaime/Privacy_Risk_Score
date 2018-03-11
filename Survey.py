# this class is the API endpoint for the
# survey page. It returns 2 JSON object
# JSON 1 - [id, question, category ]
# JSON 2 - [id, answer ]

import webapp2
import json
from QuestionsDB import Questions
from AnswersDB import Answers

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

        answers = Answers.all()
        answers.order('id')
        answersDictionary = []

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
        responses = self.request.body
        for response in responses:
            self.response.write(response)



