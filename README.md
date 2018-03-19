Privacy Risk Score back End

Descripton
This project is a backend RESTFUL services. The programing language is Python 2.7 and uses the following libraries:
.Webapp2 as a request handler.
.google.appengine.ext as a database.

How To Run
1.Download Python2.7
2.Download Google Cloud SDK
3.Create an google app engine account
4.From within the folder run dev_appserver.py app.yaml
for documentation and quickstart guide: https://cloud.google.com/appengine/docs/standard/python/quickstart

Overview
Resquest handler and routing
/survey                             main page, survey page
/score                              after completion of the survey the score is computed
/admin/addrecommendation            recommendation are assigned based on which questions were missed
/admin/dashboard                    analytics, understnading strenght and weakness of the membership around they understanding of privacy
/admin/addquestion                  add new questions for a new survey
/admin/addanswer                    add new answers for a new survey
/admin/delete                       delete all the tables in the database
/admin/memberscore                  all score by members
/admin/memberanswers                all answers by members
/admin/visits                       number of peopl who tool the survey

Database tables and relationships:

Visits(db.Model):
    id = db.IntegerProperty() PK

MemberAnswers(db.Model):
    memberID  = db.IntegerProperty() FK
    questionID = db.IntegerProperty()
    answer = db.TextProperty(required = True)
    category = db.StringProperty(required = True)
    value = db.BooleanProperty()

MemberScore(db.Model):
    memberID  = db.IntegerProperty() FK
    score = db.IntegerProperty()
-------------------------------------------------

Questions(db.Model):
    id = db.IntegerProperty() PK
    question = db.TextProperty(required = True)
    category = db.TextProperty(required = False)

Answers(db.Model):
    id = db.IntegerProperty() FK
    answer = db.TextProperty(required = True)
    category = db.TextProperty(required = False)
    value = db.BooleanProperty()
-----------------------------------------------

Recommendations(db.Model):
    link = db.TextProperty(required=True)
    category = db.TextProperty(required = True)

Computation:
ScoreCalculator.py and RecommendationEngine.py are the two classes doing computation.







