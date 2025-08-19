from question_model import Question
from main import question_bank

class QuizBrain():
    def __init__(self,question_number):
        self.question_number =1

    def next_question(self,question_number):
        print(question_bank[question_number].text)


question = QuizBrain(1)
# question.next_question(1)
print(f"Q.{question.question_number +1} {question.next_question(0)}")