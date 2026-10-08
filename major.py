import turtle
#setup the window
screen=turtle.Screen()
#bg color
screen.bgcolor("brown")
#title/name
screen.title("Neon Mandala")
screen.setup(800,800)#height and width
#setup the drawing pen
pen=turtle.Turtle()
pen.speed(0)
pen.hideturtle()
#color names
colors=["beige",  "magenta", "Aqua", "blue", "red", "green","black", "yellow", "purple", "teal"]
#start drawing
pen.penup()
pen.goto(0,0)
pen.pendown()#set pen in drawing position
pen.pensize(10)
#choose random colors
for i in range(100):
    pen.pencolor(colors[i%10])
    pen.forward(i*2)
    pen.right(91)
#Draw a petal
def petal(color):
    pen.color(color)#filled color
    pen.fillcolor(color)
    pen.begin_fill()
    pen.circle(35,60)
    pen.left(120)
    pen.circle(35,60)
    pen.left(120)
    pen.end_fill()
#petal colors
petal_colors=["beige","magenta","Aqua","blue","red","green","black","yellow","purple","teal"]
pen.penup()
pen.goto(0,250)
pen.setheading(0)
for i in range(36):
    petal(petal_colors[i%10])
    pen.penup()
    pen.goto(0,250)
    pen.right(i*10)
    pen.forward(0)
    pen.pendown()
#middle gold star
pen.penup()
pen.goto(0,-100)
pen.setheading(90)
pen.pendown()
pen.color("gold")
pen.fillcolor("gold")
pen.begin_fill()
for i in range(5):
    pen.forward(200)
    pen.right(144)
pen.end_fill()
#dot at the center
pen.penup()
pen.goto(0,0)
pen.dot(30,"white")
turtle.done()