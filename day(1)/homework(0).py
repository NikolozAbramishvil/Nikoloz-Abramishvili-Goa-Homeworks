from turtle import *

#we want to paint a house 

#step1 draw the squere
width(7)
color("purple")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
#end of square

#drawing a door

left(90)
forward(70)
color("yellow")
begin_fill()
left(90)
forward(100)
right(90)
forward(60)
right(90)
forward(100)
end_fill()
penup()
goto(200,200)
right(150)
pendown()
color("red")
begin_fill()
forward(200)
left(120)
forward(200)
end_fill()
#end of roof

penup()
goto(0,0)
pendown()
right(150)
color("purple")
forward(120)
right(90)
penup()
goto(20,120)
pendown()
color("green")
begin_fill()
forward(40)
left(90)
forward(50)
left(90)
forward(40)
left(90)
forward(50)
penup()
goto(155,120)
pendown()
right(180)
forward(50)
right(90)
forward(40)
right(90)
forward(50)
right(90)
forward(40)
end_fill()
#finish




exitonclick()