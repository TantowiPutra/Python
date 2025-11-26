from quiz_brain     import QuizBrain
from question_model import Question

from data import question_data

question_list = [Question(**x) for x in question_data]
quiz_brain    = QuizBrain(0, question_list)

while quiz_brain.still_more_question():
    quiz_brain.next_question()

print("You have completed the Quis!")
print(f'You final score was: {quiz_brain.score}/{quiz_brain.question_number}')