from google.appengine.ext import db

class ComputeCategoryPercentage:
    def compute(self, categoryToCompute):

        totalQuery = db.GqlQuery("SELECT * FROM MemberAnswers WHERE category = '%s'" %categoryToCompute)

        correctQuery = db.GqlQuery("SELECT * FROM MemberAnswers WHERE value = True AND category = '%s'" %categoryToCompute)

        totalCount = 0
        for i in totalQuery:
            totalCount += 1

        correctCount = 0
        for i in correctQuery:
            correctCount += 1

        percentage = 100 * correctCount / totalCount

        return percentage
