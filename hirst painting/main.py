import random
import turtle as t
# import colorgram
#
# colors = []
# one_color = colorgram.extract('painting.jpg', 20)
# for color in one_color:
#     rgb = color.rgb
#     colors.append((rgb[0], rgb[1], rgb[2]))
# print(colors)

colors = [(246, 243, 239), (202, 165, 108), (246, 242, 244), (149, 73, 49), (239, 245, 240), (231, 235, 240),
          (53, 93, 124), (222, 201, 137), (168, 152, 43), (134, 32, 22), (133, 163, 184), (197, 93, 72), (49, 121, 88),
          (67, 47, 40), (16, 100, 72), (146, 178, 146), (233, 176, 166), (159, 142, 158), (103, 74, 77), (20, 84, 88)]

timmy = t.Turtle()

t.colormode(255)
timmy.hideturtle()
timmy.penup()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
timmy.speed('fastest')

for steps in range(10):
    current_pos = (timmy.pos())

    for step in range(10):
        timmy.dot(20, random.choice(colors))
        timmy.forward(50)

    timmy.setpos(current_pos)
    timmy.left(90)
    timmy.forward(50)
    timmy.right(90)

screen = t.Screen()
screen.exitonclick()
