from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

screen.listen()
timmy.speed('fastest')


def move_forward():
    timmy.forward(10)


def move_backward():
    timmy.backward(10)


def move_left():
    new_heading = timmy.heading() + 10
    timmy.setheading(new_heading)


def move_right():
    new_heading = timmy.heading() - 10
    timmy.setheading(new_heading)


def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.onkey(clear, "c")
screen.exitonclick()
