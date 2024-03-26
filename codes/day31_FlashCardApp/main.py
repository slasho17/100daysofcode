from tkinter import *
import pandas
import random
#--------------------- MACROS ---------------------#
BACKGROUND_COLOR = "#B1DDC6"
FONT1 = ("Ariel", 40, "italic")
FONT2 = ("Ariel", 60, "bold")

#--------------------- GLOBALS ---------------------#
try:
    all_data = pandas.read_csv("data/words_to_learn.csv").to_dict(orient="records")
except:
    all_data = pandas.read_csv("data/french_words.csv").to_dict(orient="records")
current_card = None
timer = None

#--------------------- BUTTON COMMANDS ---------------------#
def already_know():
    global all_data, current_card
    all_data.remove(current_card)
    pandas.DataFrame(all_data).to_csv("data/words_to_learn.csv", index=False)

    next_card()

def next_card():
    global all_data, current_card, timer

    current_card = random.choice(all_data)
    canvas.itemconfig(canvas_text_language, text="French", fill="black")
    canvas.itemconfig(canvas_text_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front)
    
    try:
        window.after_cancel(timer)
    except:
        pass
    finally:
        flip_card(3)

def flip_card(counter):
    global timer
    if counter > 0:
        timer = window.after(1000, flip_card, counter - 1)
    else:
        canvas.itemconfig(canvas_image, image=card_back)
        canvas.itemconfig(canvas_text_language, text="English", fill="white")
        canvas.itemconfig(canvas_text_word, text=current_card["English"], fill="white")

#--------------------- WINDOW ---------------------#
window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#--------------------- CANVAS ---------------------#
canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")

canvas_image = canvas.create_image(400, 263, image=card_front)
canvas_text_language = canvas.create_text(400, 150, font=FONT1)
canvas_text_word = canvas.create_text(400, 263, font=FONT2)

canvas.grid(column=0, row=0, columnspan=2)

#--------------------- BUTTONS ---------------------#
right_button_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_image, highlightthickness=0, command=already_know)
right_button.grid(column=1, row=1)

wrong_button_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

#--------------------- MAIN LOOP ---------------------#
next_card()
window.mainloop()