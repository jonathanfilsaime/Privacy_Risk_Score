# this class delete both question
# and answer database

import webapp2
from QuestionsDB import Questions
from AnswersDB import Answers
from MemberAnswersDB import MemberAnswers
from MemberScoreDB import MemberScore
from VisitsDB import Visits

class Delete(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'

        questions = Questions.all()

        for question in questions:
            question.delete()

        answers = Answers.all()

        for answer in answers:
            answer.delete()

        memberAnswers = MemberAnswers.all()

        for memberAnswer in memberAnswers:
            memberAnswer.delete()

        memberScores = MemberScore.all()

        for memberScore in memberScores:
            memberScore.delete()

        visits = Visits.all()

        for visit in visits:
            visit.delete()

        self.response.write("everything got deleted")