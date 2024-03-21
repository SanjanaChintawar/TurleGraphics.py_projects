from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.upward, "Up")
screen.onkey(r_paddle.downward, "Down")
screen.onkey(l_paddle.upward, "w")
screen.onkey(l_paddle.downward, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # need to bounce
        ball.bounce_y()

    # collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #  ball miss the right paddle
    if ball.xcor() > 390:
        ball.ball_reset()
        score.l_point()

    #  ball miss the left paddle
    if ball.xcor() < -390:
        ball.ball_reset()
        score.r_point()



screen.exitonclick()
