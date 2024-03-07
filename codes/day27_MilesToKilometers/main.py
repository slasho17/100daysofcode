from tkinter import *
FONT = ("Arial", 12, "normal")
PADDING_X = 4
PADDING_Y = 1

def button_clicked():
    print("I got clicked")
    new_text = int(input.get()) * 1.609
    km_value.config(text=new_text)

window = Tk()
window.title("Miles to Km")
window.config(padx=20, pady=20)

miles = Label(text="Miles", font=FONT )
km = Label(text="Km", font=FONT, padx=PADDING_X, pady=PADDING_Y)
equals = Label(text="is equal to", font=FONT, padx=PADDING_X, pady=PADDING_Y)
km_value = Label(text="0", font=FONT, padx=PADDING_X, pady=PADDING_Y)
input = Entry(width=10)

button = Button(text="Calculate", command=button_clicked)


input.grid(row=0, column=1)
miles.grid(row=0, column=2)
equals.grid(row=1, column=0)
km_value.grid(row=1, column=1)
km.grid(row=1, column=2)
button.grid(row=2, column=1)


window.mainloop()