from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Python Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.15)
    snake.move()
    snake.head.pencolor("white")

    # collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.update_score()

    # collision with wall
    if snake.head.xcor() > 285 or snake.head.xcor() < -290 or snake.head.ycor() > 285 or snake.head.ycor() < -280:
        score.game_over()
        game_is_on = False

    # collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.game_over()
            game_is_on = False

screen.exitonclick()

