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
        self.response.write("answers have been added")

    def storeInAnswersDB(self, fileNameAndPath):
        with io.open(fileNameAndPath) as file:
            for line in file:
                element = line.split(',')
                value = False
                if element[2].rstrip() == 'true':
                    value = True

                self.response.write(element[0])
                self.response.write(element[1])
                self.response.write(element[2])

                answer = Answers(id = int(element[0]), answer = element[1], value = value, category = element[3])
                answer.put()


