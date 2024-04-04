class QuizBrain:
    def __init__(self, question_list):    
        self.question_number = 0
        self.question_list = question_list
        self.ammount = len(question_list)
        self.score = 0

    def next_question(self):
        current = self.question_list[self.question_number]
        self.question_number = self.question_number +1
        user_answer = input(f"Q.{self.question_number}: {current.text} (True or False)")
        self.check_answer(user_answer, current.answer)
        
    def still_has_questions(self):
        return self.ammount > self.question_number
    
    def check_answer(self, user_answer, right_answer):
        if user_answer.lower() == right_answer.lower():
            print("Good job")
            self.score = self.score +1
        else:
            print("Bad job")
        print(f"Your current score is {self.score}/{self.question_number}")
