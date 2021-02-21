from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = "Arial"
GREEN = "#9bdeac"
WORD_SIZE = 15
TYPE_OF_LETTER = "italic"

class QuizInterface():
    # in here we're saying that quiz_brain is an object which is of the data type QuizBrain
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz Game!")
        self.window.config(padx= 20, pady= 20, bg = THEME_COLOR)

        # Getting the whiteboard where the questions go
        self.canvas = Canvas(width=300, height=250, bg = "white", highlightthickness = 0)
        self.canvas.grid(column = 0, row= 1, columnspan = 2, pady = 30)

        # question label
        self.question_label = self.canvas.create_text(
            150,
            125,
            # we're creating this width variable so we cna actually make a line breaking and we can actually read the question
            width = 280,
            text = "Some text",
            fill = "black",
            font = (FONT, WORD_SIZE, TYPE_OF_LETTER))

        # Score Label:
        self.score_label = Label(text = "Score: 0", fg=GREEN, bg=THEME_COLOR, font=(FONT, WORD_SIZE, TYPE_OF_LETTER))
        self.score_label.grid(column = 1, row = 0)

        # True and False Buttons
        self.true_image = PhotoImage(file = "images/true.png")
        self.true_button = Button(image = self.true_image, command = self.true_answer, highlightthickness = 0)
        self.true_button.grid(column = 0, row = 2)

        self.false_image = PhotoImage(file = "images/false.png")
        self.false_button = Button(image=self.false_image, command = self.false_answer, highlightthickness=0)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white", highlightthickness=0)
        if self.quiz.still_has_questions():
            self.score_label.config(text = f"Score: {self.quiz.score}")
            # the reason why is not appearing any suggestion from Pycharm is because the code doesn't know which
            # data type is quiz_brain (parameter given in the init.
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_label, text= q_text)
        else:
            self.canvas.itemconfig(self.question_label, text= "You've reached the end of the quiz")
            self.true_button.config(state = "disabled")
            self.false_button.config(state = "disabled")

    def true_answer(self):
        answer_given = "True"
        answer = self.quiz.check_answer(user_answer= answer_given)
        self.give_feedback(answer)

    def false_answer(self):
        answer_given = "False"
        answer = self.quiz.check_answer(user_answer=answer_given)
        self.give_feedback(answer)

    def give_feedback(self, answer):
        if answer:
            self.canvas.config(bg="green", highlightthickness = 0)
        else:
            self.canvas.config(bg="red", highlightthickness = 0)
        self.window.after(1000, self.get_next_question)