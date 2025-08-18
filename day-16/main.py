# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
#
from prettytable import PrettyTable
tabel = PrettyTable()
tabel.add_column('Pokemon name', ["Pikachu","Squirtle","Charmander"],)
tabel.add_column("Type", ["Electric","water","Fire"])
print(tabel.align)
tabel.align = "l"
print(tabel.align)
print(tabel)