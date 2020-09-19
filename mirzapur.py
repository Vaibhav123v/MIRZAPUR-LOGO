import turtle
t = turtle.Turtle()

turtle.bgcolor("white")
t.up()
t.goto(620,0)
t.down()
t.pensize(2)
t.color("darkred")
t.fillcolor("black")
t.begin_fill()
t.setheading(90)
t.goto(620,300)
t.setheading(180)
t.goto(-620,300)
t.setheading(270)
t.goto(-620,-300)
t.setheading(0)
t.goto(620,-300)
t.setheading(90)
t.goto(620,0)
t.end_fill()
t.up()
t.goto(-600,0)
t.down()
t.setheading(0)
t.fillcolor("#FF0000")
t.begin_fill()
t.goto(-600,200)#upper
t.goto(-570,200)
t.goto(-530,40)
t.goto(-490,200)
t.goto(-460,200)
#t.goto(-580,0)
#t.goto(-600,0)

#t.goto(-460,0)
t.goto(-460,0)
t.goto(-485,0)
t.goto(-485,150)#second upper
t.goto(-520,0)
t.goto(-540,0)
t.goto(-575,150)
t.goto(-575,0)
t.goto(-600,0)
t.end_fill()

#t.goto(-480,200)#second upper
#t.goto(-460,200)
#t.goto(-530,130)
#t.goto(-580,160)
#t.goto(-580,0)
#t.goto(-600,0)
##############################################################################i

t.up()
t.fillcolor("#FF0000")
t.begin_fill()
t.goto(-450,0)
t.down()
t.goto(-310,0)
t.goto(-310,25)
t.goto(-367.5,25)
t.goto(-367.5,175)
t.goto(-310,175)
t.goto(-310,200)
t.goto(-450,200)
t.goto(-450,175)
t.goto(-390.5,175)
t.goto(-390.5,25)
t.goto(-450,25)
t.goto(-450,0)
t.end_fill()

t.color("darkred")
###############################################################################
t.up()
t.goto(-300,0)
t.down()
t.fillcolor("red")
t.begin_fill()
t.goto(-300,200)
t.goto(-250,200)
a = 360
for i in range(9):
    a = a-20
    t.setheading(a)
    t.forward(20)
t.goto(-160,-20)
t.goto(-220,0)
t.goto(-270,50)
t.goto(-270,0)
t.goto(-300,0)
t.end_fill()
########
t.up()
t.goto(-270,110)
t.down()
t.fillcolor("black")
t.begin_fill()
t.goto(-270,180)
t.setheading(0)
t.forward(15)
q = 360
for i in range(9):
    q =q-20
    t.setheading(q)
    t.forward(12.5)
t.goto(-270,110)
t.end_fill()
#t.goto(-160,0)/*

#########################################################################3Z
t.setheading(0)
t.up()
t.fillcolor("#FF0000")
t.begin_fill()
t.goto(-150,0)
t.down()
t.goto(-10,0)
t.goto(-10,25)
t.goto(-100,25)
t.goto(-10,200)
t.goto(-150,200)
t.goto(-150,175)
t.goto(-50,175)
t.goto(-150,0)
t.end_fill()
###############################################################################

t.up()
t.goto(-10,0)
t.goto(0,0)
t.fillcolor("#FF0000")
t.begin_fill()
t.down()
t.goto(50,200)
t.goto(90,200)
t.goto(140,0)
t.goto(115,0)
t.goto(70,150)
t.goto(25,0)
t.goto(0,0)
t.end_fill()
t.goto(25,0)
t.fillcolor("red")
t.begin_fill()
t.goto(40,50)
t.goto(100,50)
t.goto(95,60)
t.goto(45,60)
t.end_fill()
#######################################################
t.up()
t.goto(160,0)
t.down()
t.fillcolor("red")
t.begin_fill()
t.goto(160,200)
t.goto(210,200)
t.setheading(0)
an =360
for i in range(9):
    an=an-20
    t.setheading(an)
    t.forward(20)
t.forward(5)    
t.goto(185,-20)
t.goto(160,0)
t.end_fill()
t.up()
t.goto(185,110)
t.down()
t.fillcolor("black")
t.begin_fill()
t.goto(185,180)
t.setheading(0)
t.forward(15)
p = 360
for i in range(9):
    p =p-20
    t.setheading(p)
    t.forward(12.5)
t.goto(185,110)
t.end_fill()
#################################P
t.up()
t.goto(300,45)

t.down()
t.fillcolor("#FF0000")
t.begin_fill()
t.goto(300,200)
t.goto(325,200)
t.goto(325,45)
b= 270
for i in range(9):
    b = b+20
    t.setheading(b)
    t.forward(15)

t.goto(410,200)
t.goto(435,200)
t.goto(435,45)
c = 270

for i in range(9):
    c = c-20
    t.setheading(c)
    t.forward(23.7)

t.end_fill()
#################################################
#t.up()
#t.goto(450,0)
#t.down()
#t.goto(590,0)
#t.up()
#t.goto(0,-250)
#t.down()
#33
t.up()
t.goto(450,0)
t.fillcolor("red")
t.begin_fill()
t.down()
t.goto(450,200)

#t.goto(-300,0)
#t.down()
#t.goto(-300,200)
t.goto(500,200)
v = 360
for i in range(9):
    v = v-20
    t.setheading(v)
    t.forward(20)
t.goto(590,-20)
t.goto(530,0)
t.goto(480,50)
t.goto(480,0)
t.goto(450,0)
t.end_fill()
########
t.up()
t.goto(480,110)
t.down()
t.fillcolor("black")
t.begin_fill()
t.goto(480,180)
t.setheading(0)
t.forward(15)
q = 360
for i in range(9):
    q =q-20
    t.setheading(q)
    t.forward(12.5)
t.goto(480,110)
t.end_fill()




