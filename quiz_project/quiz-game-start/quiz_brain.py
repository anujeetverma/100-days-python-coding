
class QuizBrain():
    def __init__(self,q_list):
        self.question_number =0
        self.score=0
        self.user_response=''
        self.question_list = q_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        self.user_response= input(f"Q.{self.question_number } {current_question.text} (True/False): ").title().strip()

    def check_answer(self):
        if self.user_response == self.question_list[self.question_number-1].answer:
            self.score +=1
            print(f"Your answer is correct{self.score}/{self.question_number}")
        else:
            print(f"Your answer is wrong{self.score}/{self.question_number}")


    def still_has_questions(self):
        while self.question_number in range(len(self.question_list) ):
            self.next_question()
            self.check_answer()

# question.next_question(1)
