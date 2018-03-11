from AnswersDB import Answers

class ScoreCalculator:

    def computeScore(self, responseArray):

        answers = Answers.all()
        answers.order('id')

        valueTable = []
        for answer in answers:
            if answer.value:
                valueTable.append(answer.answer.rstrip())

        index = 0
        score = 0
        while index < len(responseArray):
            if responseArray[index] == valueTable[index]:
                score += 1
            index += 1

        return score