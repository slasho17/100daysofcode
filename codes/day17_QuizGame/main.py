from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questions = []
for data in question_data:
    new_q = Question(data['text'], data['answer'])
    questions.append(new_q)
    
quiz = QuizBrain(questions)
quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()
    
print("You finished the quiz!")