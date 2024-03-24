import turtle
import pandas

image = "map.gif"
screen = turtle.Screen()
screen.title("Guess States of India")
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("states.csv")
all_state_list = data["state"].to_list()
user_guessed_states = []

keep_guessing = True
while keep_guessing:
    user_answer = screen.textinput(title=f"{len(user_guessed_states)}/31 correct states",
                                   prompt="What's the another state name? ").title()
    if user_answer == "Exit":
        break
    elif user_answer in all_state_list:
        user_guessed_states.append(user_answer)
        user_state = data[data["state"] == user_answer]
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        tim.goto(int(user_state.x.item()), int(user_state.y.item()))
        tim.write(arg=f"{user_answer}", align="center", font=("Arial", 13, "bold"))
    else:
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        tim.goto(0,0)
        tim.write(arg=f"Your Final Score is {len(user_guessed_states)}", align="center", font=("Arial", 43, "bold"))
        keep_guessing = False

screen.exitonclick()