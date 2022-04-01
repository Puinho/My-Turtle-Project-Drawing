import turtle
from turtle import *

tela = turtle.Screen()

tela.bgcolor("pink")

tela.setup(600, 500)
shape("turtle")
color("black")
width(5)
speed(1)

penup()
back(5)
right(90)
fd(180)
left(90)
pendown()

begin_fill()
fillcolor("red")
pensize(3)
left(50)
forward(266)
circle(100,200)
right(140)
circle(100,200)
forward(266)
end_fill()

penup()
right(40)
setpos(0, 60)
left(90)
back(4)
right(90)



Fonte = ("Cheri Liney", 8, "bold")
write("i", False, "center", Fonte)
fd(60)
write("love", False, "center", Fonte)
fd(60)
write("you", False, "center", Fonte)
fd(60)

setpos(80, 0)
left(180)
back(120)
right(180)
#time.sleep(100)

pendown()
begin_fill()
fillcolor("white")
fd(75)
left(90)
fd(160)
left(90)
fd(75)
left(90)
fd(160)
left(90)
penup()
fd(30)
left(90)
fd(10)
right(90)
end_fill()

Fonte2 = ("Arial", 3, "bold")
write("Turtle Project", False, "left", Fonte2)
fd(30)
write("github.com/puinho", False, "left", Fonte2)

hideturtle()
turtle.done()