import webapp2
from MemberAnswersDB import MemberAnswers

class ViewMembersAnswers(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        memberAnswers = MemberAnswers.all()
        # memberAnswers.order('memberID' and 'questionID')
        memberAnswers.order('memberID')
        # memberAnswers.order('questionID')

        for ma in memberAnswers:
            self.response.write("\n")
            self.response.write(ma.memberID)
            self.response.write("\n")
            self.response.write(ma.questionID)
            self.response.write("\n")
            self.response.write(ma.answer)
            self.response.write("\n")
            self.response.write(ma.value)
            self.response.write("\n")
            self.response.write(ma.category)
            self.response.write("\n")
            self.response.write("-----------")

