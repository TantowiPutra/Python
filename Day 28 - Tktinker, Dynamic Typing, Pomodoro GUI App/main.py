from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

timer = None
reps = 0
work_sessions = 0
current_session = ""

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global is_timer_start, timer, reps, work_sessions, current_session, timer_label, checkmark

    if timer:
        window.after_cancel(timer)
        is_timer_start  = False

        canvas.itemconfig(timer_text, text="00:00")
        timer_label.config(text="TIMER", font=("Roboto", 36, "bold"), fg=GREEN)
        checkmark.config(text="")

        reps            = 0
        work_sessions   = 0
        current_session = ""
        timer           = None

# ---------------------------- TIMER MECHANISM ------------------------------- #
is_timer_start = False
def start_timer():
    global is_timer_start, reps, current_session

    if is_timer_start:
        return

    reps += 1

    work_sec        = WORK_MIN * 1
    short_break_sec = SHORT_BREAK_MIN * 1
    long_break_sec  = LONG_BREAK_MIN * 1

    is_timer_start = True
    if reps % 4 == 0:
        current_session = "LONG BREAK"
        timer_label.config(text="LONG BREAK", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        current_session = "SHORT BREAK"
        timer_label.config(text="SHORT BREAK", fg=PINK)
        count_down(short_break_sec)
    else:
        current_session = "WORK"
        timer_label.config(text="WORK", fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global is_timer_start, reps, current_session, work_sessions, timer
    minutes = count // 60
    seconds = count % 60

    if minutes < 10:
        minutes = f"0{minutes}"

    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")

    if count > 0 and is_timer_start:
        timer = window.after(1000, count_down, count - 1)
    else:
        if current_session == "WORK":
            work_sessions += 1
            checkmark.config(text="✓" * work_sessions)

        is_timer_start = False
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas Widget
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image  = PhotoImage(file="./tomato.png")
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Label
timer_label = Label(text="TIMER", font=("Roboto", 36, "bold"), fg=GREEN, bg=YELLOW, width=12)
timer_label.grid(row=0, column=1)

checkmark = Label(fg=GREEN, bg=YELLOW, font=("Roboto", 36, "normal"))
checkmark.grid(row=3, column=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(row=2, column=2)

window.mainloop()