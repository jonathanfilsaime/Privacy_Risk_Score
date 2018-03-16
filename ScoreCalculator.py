from AnswersDB import Answers
from MemberAnswersDB import MemberAnswers
from MemberScoreDB import  MemberScore

class ScoreCalculator:

    def computeScore(self, responseArray, memberID):

        answers = Answers.all()
        answers.order('id')

        valueTable = []
        categoryTable = []
        for answer in answers:
            if answer.value:
                valueTable.append(answer.answer.rstrip())
                categoryTable.append(answer.category.rstrip())

        index = 0
        score = 0
        while index < len(responseArray):

            value = False
            if responseArray[index] == valueTable[index]:
                value = True
                score += 1

            memberAnswer = MemberAnswers(memberID = memberID, questionID = (index+1), answer = responseArray[index], value = value, category = categoryTable[index])
            memberAnswer.put()
            index += 1

        scorePercentage = 100 * score / index

        memberScore = MemberScore(memberID = memberID, score = scorePercentage)
        memberScore.put()

        return scorePercentage