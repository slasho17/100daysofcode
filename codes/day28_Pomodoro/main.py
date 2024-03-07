from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
MIN = 60
reps = 1
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_command():
    global reps
    reps = 1
    global window
    window.after_cancel(timer)
    canvas.itemconfig(canvas_text, text="00:00")
    msg.config(text="Pomodoro")
    check.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_command():
    global msg
    if  reps % 8 == 0:
        msg.config(text="Hora de fumar umzinho")
        count_down(LONG_BREAK_MIN)
        check.config(text="🗸 " * int(reps/2))
    elif reps % 2 == 0:
        msg.config(text="Go have fun bitch")
        count_down(SHORT_BREAK_MIN)
        check.config(text="🗸 " * int(reps/2))
    else:
        msg.config(text="Work bitch")
        count_down( WORK_MIN)
        
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(counter):
    global timer
    global reps
    clock_string = f"{math.floor(counter / MIN)}:{counter%MIN if counter%MIN > 9 else f'0{counter%MIN}'}"
    canvas.itemconfig(canvas_text, text=clock_string)
    if counter > 0:
        timer = window.after(1000, count_down, counter - 1)
    else:
        reps += 1
        print(reps)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady= 50, bg=YELLOW)


msg = Label(text="Work bitch", font=(FONT_NAME, 40, "bold"), fg=RED, bg=YELLOW)
msg.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image = image)
canvas_text = canvas.create_text(100, 130, text = "00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)
button_start = Button(text="Start", command=start_command, highlightthickness=0)
button_start.focus()
button_start.grid(row=2, column=0)
button_reset = Button(text="Reset", command=reset_command, highlightthickness=0)
button_reset.grid(row=2, column=2)

check = Label(text="", font=(FONT_NAME, 25, "bold"), fg=GREEN, bg=YELLOW)
check.grid(row=3, column=1)

window.mainloop()