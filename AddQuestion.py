import webapp2

class AddQuestion(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('AddQuestion Page')