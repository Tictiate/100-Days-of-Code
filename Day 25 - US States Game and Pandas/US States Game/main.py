import turtle
import os
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
image = os.path.join(script_dir, "blank_states_img.gif")
screen.addshape(image)
turtle.shape(image)

#Game Logic
data = pandas.read_csv(os.path.join(script_dir, "50_states.csv"))
states = data["state"].to_list()
correct_answers = []

t = turtle.Turtle()
t.pu()
t.hideturtle()

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
while len(correct_answers) != 50:
    if answer_state == "Exit":
        states_to_learn = []
        for state in states:
            if state not in correct_answers:
                states_to_learn.append(state)
        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn.csv") 
        break
    if answer_state.title() in states and answer_state.title() not in correct_answers:
        r = data[data["state"] == answer_state.title()].iloc[0]
        t.goto(r["x"], r["y"])
        t.write(answer_state.title())
        correct_answers.append(answer_state.title())
        answer_state = screen.textinput(title=f"{len(correct_answers)}/50 States Correct", prompt="What's another state's name?")

