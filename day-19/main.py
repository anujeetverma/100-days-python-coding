from turtle import Turtle,Screen
import random

screen = Screen()
screen.setup(width=500,height=400)
user_bet= screen.textinput(title="Make your bet",prompt= "which turtle will win the race? Enter a color: ")

tim0 = Turtle(shape="turtle")
tim0.color("violet")
tim0.penup()

tim1 = Turtle(shape="turtle")
tim1.color("indigo")
tim1.penup()

tim2 = Turtle(shape="turtle")
tim2.color("blue")
tim2.penup()

tim3 = Turtle(shape="turtle")
tim3.color("green")
tim3.penup()

tim4 = Turtle(shape="turtle")
tim4.color("yellow")
tim4.penup()

tim5 = Turtle(shape="turtle")
tim5.color("orange")
tim5.penup()

tim6 = Turtle(shape="turtle")
tim6.color("red")
tim6.penup()



tim0.goto(x= -200,y= -150)
tim1.goto(x= -200,y= -100)
tim2.goto(x= -200,y= -50)
tim3.goto(x= -200,y= 0)
tim4.goto(x= -200,y= 50)
tim5.goto(x= -200,y= 100)
tim6.goto(x= -200,y= 150)


all_turtle=[tim0,tim1,tim2,tim3,tim4,tim5,tim6]

is_race_on =False
if user_bet:
    is_race_on=True


while is_race_on:
    for turtle in all_turtle:
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
        if turtle.xcor()>220:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! {winning_color}")
                is_race_on = False
            else:
                print(f"you lost! {winning_color} is the winner ")
            is_race_on = False


screen.exitonclick()
