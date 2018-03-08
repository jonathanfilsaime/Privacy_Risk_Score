import webapp2
from MainPage import MainPage
from Survey import Survey
from Score import Score
from Recommendation import Recommendation
from Admin import Admin
from AddQuestion import AddQuestion
from AddAnswer import AddAnswer
from Delete import Delete

app = webapp2.WSGIApplication([('/', MainPage),
                               ('/survey', Survey),
                               ('/score', Score),
                               ('/recommendation', Recommendation),
                               ('/admin', Admin),
                               ('/admin/addquestion', AddQuestion),
                               ('/admin/addanswer', AddAnswer),
                               ('/admin/delete', Delete)
                                ], debug=True)
