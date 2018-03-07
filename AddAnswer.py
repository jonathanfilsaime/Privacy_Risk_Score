import webapp2

class AddAnswer(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('AddAnswer Page')