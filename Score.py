import webapp2

class Score(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        score = str(self.request.cookies.get('score'))
        self.response.write(score)