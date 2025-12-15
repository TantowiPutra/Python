from tkinter import *

# 1. Initialize Window
window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=250, height=100)
window.config(padx=30, pady=30)

# 2. Create Entry
entry = Entry(width=10)
entry.grid(row=0, column=1)

# 3. Create Labels
first_label = Label(text="Miles", font=("Arial", 12, "normal"))
first_label.grid(row=0, column=2)

second_label = Label(text="is equal to", font=("Arial", 12, "normal"))
second_label.grid(row=1, column=0)

third_label = Label(text="0", font=("Arial", 12, "normal"))
third_label.grid(row=1, column=1)

fourth_label = Label(text="Km", font=("Arial", 12, "normal"))
fourth_label.grid(row=1, column=2)

# 4. Button
def convert_mile():
    MILE_TO_KM = 1.60934
    curr_mile = entry.get()
    third_label.config(text=int(curr_mile) * MILE_TO_KM)

button = Button(text="Click Me!", command=convert_mile)
button.grid(row=2, column=1)


window.mainloop()
