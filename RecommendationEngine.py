from MemberAnswersDB import MemberAnswers
from RecommendationsDB import Recommendations

class RecommendationEngine():
    def recommend(self, memberID):

        categories = {
            "credit monitoring" : True,
            "authentication" : True,
            "social media" : True,
            "devices" : True
        }
        memberAnswers = MemberAnswers.all()
        memberAnswers.order('-value')
        for memberAnswer in memberAnswers:
            if memberAnswer.memberID == memberID:
                if memberAnswer.value == False:
                    categories[memberAnswer.category] = False

        category = []
        if not categories["credit monitoring"]:
            category.append("credit monitoring")
        if not categories["authentication"]:
            category.append("authentication")
        if not categories["social media"]:
            category.append("social media")
        if not categories["devices"]:
            category.append("devices")

        recommendations = Recommendations.all()

        recommendationDictionary = []
        for recommendation in recommendations:
            if recommendation.category.rstrip() in category:
                recDic = {
                    'recommendation' : recommendation.recommendation,
                    'link' : recommendation.link,
                    'category' : recommendation.category
                }
                recommendationDictionary.append(recDic)

        return recommendationDictionary






