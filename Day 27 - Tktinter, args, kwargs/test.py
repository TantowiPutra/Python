from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# 1. Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
# my_label.pack()
# my_label.place(relx=0.5, rely=0.1, anchor="center")
my_label.grid(column=0, row=0)

""" Modifying Label Text """
my_label["text"] = "New text"
my_label.config(text="New Text")

# 2. Buttons
def button_clicked():
    print("I got clicked")
    my_label.config(text="Button Got Clicked")

    text_input = inp.get()
    window.title(text_input)

button = Button(text="Click Me!", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

button2 = Button(text="Click Me!", command=button_clicked)
# button.pack()
button2.grid(column=2, row=0)

# 3. Entry
inp = Entry(width=30)
inp.insert(END, "Hello, World!")
# inp.pack(pady=(10, 0))
inp.grid(column=3, row=2)

window.mainloop()