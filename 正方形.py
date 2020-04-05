import turtle
t=turtle.Pen()
t.setpos(-1,-200)
colors=["red","orange","yellow","green"]
turtle.bgcolor("black")
for i in range(16):
    t.pencolor(colors[i%4])
    t.forward(100)
    t.left(22.5)
#turtle.exitonclick()
turtle.done()