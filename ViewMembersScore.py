import webapp2
from MemberScoreDB import MemberScore

class ViewMembersScore(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        memberScore = MemberScore.all()
        memberScore.order('memberID')

        for ms in memberScore:
            self.response.write("\n")
            self.response.write(ms.memberID)
            self.response.write("\n")
            self.response.write(ms.score)
            self.response.write("\n")
            self.response.write("---------------")
