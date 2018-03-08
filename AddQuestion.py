import webapp2
import io

class AddQuestion(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.readFile("questions.txt")

    def readFile(self, fileNameAndPath):
        with io.open(fileNameAndPath) as file:
            for line in file:
                self.response.write(line)
