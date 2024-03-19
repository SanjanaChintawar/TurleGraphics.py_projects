from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=600, height=500)
user_guess = screen.textinput(title="Make your bet.", prompt="Who will win the race? bet a color (from rainbow): ")

all_turtles = []
colors = ["orange", "blue", "green", "red", "yellow", "purple"]
y_pos = [-100, -60, -20, 20, 60, 100]
for num in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.fillcolor(colors[num])
    new_turtle.goto(x=-270, y=y_pos[num])
    all_turtles.append(new_turtle)

if user_guess:
    is_race_on = Turtle

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 270:
            is_race_on = False
            winning_color = turtle.fillcolor()
            if winning_color == user_guess:
                print(f"You won, The winner is {user_guess} Turtle")
            else:
                print(f"You lost, The winner is {winning_color} Turtle")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
