# this class delete both question
# and answer database

import webapp2
from QuestionsDB import Questions
from AnswersDB import Answers

class Delete(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'

        questions = Questions.all()

        for question in questions:
            question.delete()

        answers = Answers.all()

        for answer in answers:
            answer.delete()