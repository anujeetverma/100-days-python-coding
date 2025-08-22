from turtle import Turtle,Screen
import heroes
from random import randint,random
from hirst_painitng import extracted_colors

tim = Turtle()
angles = [0,90,180,270]
tim.shape("circle")
tim.speed(20)
tim.pensize(3)

# tim.color("aquamarine")
tim.hideturtle()

angle =0
for i in range(36):
    tim.circle(100)
    tim.right(angle)

    angle+=1

    tup = (random(), random(), random())
    tim.pencolor(tup)


# for j in range (0,100):
#     for i in range (j):
#         tim.forward(15)
#         tim.right(angles[randint(0,3)])
#         tup = (random(), random(), random())
#         tim.pencolor(tup)



print(heroes.gen())

screen = Screen()
screen.exitonclick()