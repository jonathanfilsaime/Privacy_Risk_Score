import webapp2

class Score(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Score Page')
        score = str(self.request.cookies.get('score'))
        self.response.write(score)