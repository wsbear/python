import random
import turtle

t=turtle.Pen()
turtle.Turtle().screen.delay(0)
turtle.bgcolor("black")
colors=["red","yellow","blue","green","orange","purple","white","grey","cyan"]

for n in range(500):
    
    t.pencolor(random.choice(colors))
    size=random.randint(10,40)

    x=random.randrange(-turtle.window_width()//2,turtle.window_width()//2)
    y=random.randrange(-turtle.window_height()//2,turtle.window_height()//2)

    t.penup()
    t.setpos(x,y)
    t.pendown()

    for m in range(size):
        t.pencolor(colors[m%9])
        t.forward(m*2)
        t.left(190)

