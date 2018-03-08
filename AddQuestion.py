# this class read from a file and populates the
# database table QuestionDb
# this is strictly for admin use

import webapp2
import io
from QuestionsDB import Questions

class AddQuestion(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.storeInQuestionDb("questions.txt")

    def storeInQuestionDb(self, fileNameAndPath):
        with io.open(fileNameAndPath) as file:
            for line in file:
                element = line.split(',')
                question = Questions(id = int(element[0]), question = element[1], category = element[2])
                question.put()

