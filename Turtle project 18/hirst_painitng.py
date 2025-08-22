import turtle

from colorgram import extract
from turtle import Turtle,Screen
from random import randint

no_of_colors =20
colors = extract('herst_painting.jpg', no_of_colors)

extracted_colors = []
for i in range (no_of_colors):
    first_color = colors[i]
    extracted_colors.append((first_color.rgb.r,first_color.rgb.g,first_color.rgb.b))
# print(extracted_colors)



screen = Screen()

no_of_rows =20
no_of_columns =20

tim =Turtle()
tim.penup()
tim.goto(-330, -200)  # Move to coordinates (100, 50)
turtle.colormode(255)
tim.pensize(15)

for rows in range(no_of_rows):
    for cols in range(no_of_columns):
        color_picker = randint(0, no_of_colors)
        tup = extracted_colors[color_picker-1]
        tim.pencolor(tup)
        tim.pendown()
        tim.forward(3)
        tim.penup()
        tim.forward(30)
    tim.right(180)
    tim.penup()
    tim.forward(33*no_of_columns)
    tim.right(90)
    tim.forward(30)
    tim.right(90)












screen.exitonclick()