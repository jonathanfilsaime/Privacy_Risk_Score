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
                value = False
                if element[2] == 'true':
                    value = True
                answer = Answers(id = int(element[0]), answer = element[1], value = value)
                answer.put()
