from Tools.scripts.texi2html import increment


class QuizBrain:
    def __init__(self, question_number, question_list):
        self.question_number = question_number
        self.question_list   = question_list
        self.score           = 0

    def still_more_question(self):
        return self.question_number != len(self.question_list)

    @staticmethod
    def check_answer(answer, correct_answer):
        return correct_answer.lower() == answer.lower()

    def increment_score(self):
        self.score += 1

    def next_question(self):
        question_number = self.question_number
        question        = self.question_list[question_number]
        ans = input(f"Q.{question_number + 1} {question.text} (True or False): ").lower()

        self.question_number += 1

        if self.check_answer(ans, question.answer):
            print("You got it right!")
            self.increment_score()
        else:
            print("That's wrong.")
            print(f"The Correct Answer was {question.answer}")

        print(f"Your current score is: {self.score}/{self.question_number}\n")