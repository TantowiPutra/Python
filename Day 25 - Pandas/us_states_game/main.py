from turtle import Screen, Turtle
from datetime import datetime
import pandas

screen = Screen()
screen.title("U.S. States Game")
image = "./blank_states_img.gif"
screen.addshape(image)
screen.tracer(0)

t = Turtle()
t.shape(image)

pen = Turtle()
pen.hideturtle()
pen.penup()
screen.update()

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# screen.onscreenclick(get_mouse_click_coor)
# screen.mainloop()

def get_state_data():
    data = pandas.read_csv('./50_states.csv')
    return data

def write_map(state, x, y):
    pen.goto((x, y))
    pen.write(f"{state}", align="center", font=("Courier", 10, "bold"))
    screen.update()

state_data      = get_state_data()
is_game_running = True
guessed_states  = []

while is_game_running:
    is_game_running = False
    answer_state = screen.textinput(title=f"Guess the State! {len(guessed_states)}/50", prompt="What's another state's name?")

    if answer_state is None:
        break

    answer_state = answer_state.title()

    is_found     = state_data[state_data.state == answer_state]

    if not is_found.empty:
        write_map(is_found.iloc[0]['state'], is_found.iloc[0]['x'], is_found.iloc[0]['y'])
        guessed_states.append(answer_state)

        is_game_running = True

print(~state_data['state'].isin(guessed_states))
not_guessed = state_data[~state_data['state'].isin(guessed_states)]

filename = f"not_guessed_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
not_guessed.to_csv(filename)
