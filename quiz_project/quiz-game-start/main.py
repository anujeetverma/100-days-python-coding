from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for element in question_data:
    question = element["text"]
    answer = element["answer"]
    new_question = Question(question,answer)
    question_bank.append(new_question)

# print(question_bank[1].text)
quiz =QuizBrain(question_bank)
quiz.still_has_questions()