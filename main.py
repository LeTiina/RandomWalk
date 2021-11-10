import random
from turtle import Turtle,Screen

timmy = Turtle()


def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    timmy.color(R, G, B)
    timmy.pensize(10)
    timmy.speed(100)


while True:
    value = random.randint(1,4)
    change_color()
    if value == 1:
        timmy.left(90)
        timmy.forward(20)
    elif value == 2:
        timmy.back(20)
    elif value == 3:
        timmy.forward(20)
    else:
        timmy.right(90)
        timmy.forward(20)

screen = Screen()
screen.exitonclick()

