from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT = ("Ariel", 20, "italic")

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.score_label = Label(text="Score: 0", bg = THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)
        
        self.canvas = Canvas(height=250, width=300, bg='white')
        self.canvas_text = self.canvas.create_text(
            150 ,125,
            font=FONT,
            text="Dummy",
            fill=THEME_COLOR,
            width=280)        
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        
        self.get_next_question()
        self.right_button_image = PhotoImage(file="images/true.png")
        self.right_button = Button(image=self.right_button_image, highlightthickness=0, command=self.true_pressed, bg=THEME_COLOR)
        self.right_button.grid(column=1, row=2)

        self.wrong_button_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=self.wrong_button_image, highlightthickness=0, command=self.false_pressed, bg=THEME_COLOR)
        self.wrong_button.grid(column=0, row=2)
        
        self.window.mainloop()
        
    def true_pressed(self):
        self.check_answer(self.quiz_brain.check_answer("true"))
    def false_pressed(self):
        self.check_answer(self.quiz_brain.check_answer("false"))
        
    def get_next_question(self):
        q_text = self.quiz_brain.next_question()
        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.canvas_text, fill="black")
        self.canvas.itemconfig(self.canvas_text, text=q_text)

    def check_answer(self, got_it_right: bool):
        if got_it_right:
            self.quiz_brain.score += 1
            self.canvas.config(bg="Green")
        else:
            self.canvas.config(bg="Red")
        self.canvas.itemconfig(self.canvas_text, fill="white")
        self.score_label.config(text=f"Score: {self.quiz_brain.score}")
        self.window.after(1000, self.get_next_question)