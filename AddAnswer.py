# this class read from a file and populates the
# database table AnswersDB
# this is strictly for admin use

import webapp2
import io
from AnswersDB import Answers

class AddAnswer(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.storeInAnswersDB("answers.txt")

    def storeInAnswersDB(self, fileNameAndPath):
        with io.open(fileNameAndPath) as file:
            for line in file:
                element = line.split(',')
                i = 0
                while i < len(element):
                    question = Answers(id = int(element[0]), answer = element[i])
                    question.put()
                    i += 1
