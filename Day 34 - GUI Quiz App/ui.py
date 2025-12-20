from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        # INIT QUIZ BRAIN
        self.quiz_brain = quiz_brain

        # INIT WINDOW
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg="#0c315d", padx=20, pady=20)
        self.is_processing = False

        # QUESTION CANVAS
        self.q_canvas = Canvas(
            width=300,
            height=250,
            bg="white",
            highlightthickness=0
        )
        self.q_canvas.grid(row=1, column=0, columnspan=2)

        # SCORE LABEL
        self.score_label = Label(text="Score: 0", fg="white", bg="#0c315d", font=('Arial', 18, 'bold'))
        self.score_label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

        self.q_canvas_text = self.q_canvas.create_text(
            150,
            125,
            text="Amazon Acquired Twitch in August 2014 for $970 million dollars.",
            fill="#0c315d",
            font=('Arial', 14, 'italic'),
            width=280,
            anchor="center"
        )

        # TRUE FALSE BTN
        true_img = PhotoImage(file="./images/true.png")
        self.true_btn = Button(image=true_img, command=lambda: self.check_answer("True"))
        self.true_btn.grid(row=2, column=0, pady=20)

        false_img = PhotoImage(file="./images/false.png")
        self.false_btn = Button(image=false_img, command=lambda: self.check_answer("False"))
        self.false_btn.grid(row=2, column=1, pady=20)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.q_canvas.config(bg="white")

        q_test = self.quiz_brain.next_question()
        self.q_canvas.itemconfig(self.q_canvas_text, text=q_test)
        self.is_processing = False


    def check_answer(self, answer):
        if not self.is_processing:
            if self.quiz_brain.still_has_questions():
                self.is_processing = True
                is_true, score = self.quiz_brain.check_answer(answer)

                if not is_true:
                    self.q_canvas.config(bg="red")
                else:
                    self.q_canvas.config(bg="green")

                self.score_label.config(text=f"Score: {score}")
                self.window.after(1000, self.get_next_question)
            else:
                self.q_canvas.itemconfig(self.q_canvas_text, text="You've reached the end of the quiz")

