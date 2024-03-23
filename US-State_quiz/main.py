import turtle as t
import pandas

screen = t.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
t.shape(image)

states_data = pandas.read_csv("50_states.csv")
all_states_list = states_data["state"].to_list()
user_answer_list = []
score = 0

while len(user_answer_list) < 50:
    user_answer = screen.textinput(title=f"Guessed {score}/50 correct", prompt="What's the another State?").title()

    if user_answer == "Exit":
        for item in user_answer_list:
            all_states_list.remove(item)
        data = pandas.DataFrame(all_states_list)
        data.to_csv("Missing_states.csv")
        break

    if user_answer in all_states_list:
        user_answer_list.append(user_answer)
        user_state = states_data[states_data["state"] == user_answer]
        tim = t.Turtle()
        tim.hideturtle()
        tim.penup()
        tim.goto(int(user_state.x.item()), int(user_state.y.item()))
        tim.write(f"{user_answer}", align="center", font=("Arial", 15, "normal"))
        score += 1

