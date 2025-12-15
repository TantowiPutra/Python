from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# 1. Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()

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
button.pack()

# 3. Entry
inp = Entry(width=30)
inp.insert(END, "Hello, World!")

inp.pack(pady=(10, 0))

# 4. Text
text = Text(height=5, width=30)
text.focus()
text.insert(END, "Example of multi-line text entry.")
print(text.get("1.0", END))

text.pack(pady=(10, 0))

# Spinbox
def spinbox_used():
    print(spinbox.get())

spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

# Scale
def scale_used(value):
    print(value)

scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

# Checkbox
def checkbutton_used():
    print(checked_state.get())

checked_state = IntVar()
check_button = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
check_button.pack()

# Radio Button
def radio_used():
    print(radio_state.get())

radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

# Listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]

for item in fruits:
    listbox.insert(fruits.index(item), item)

listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()