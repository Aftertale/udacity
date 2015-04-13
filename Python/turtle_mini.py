import turtle

def drawTriangle(someTurtle, length):
    for i in range(0,3):
        someTurtle.forward(length)
        someTurtle.right(240)

def drawFractal(degree):
    window = turtle.Screen()
    brad = turtle.Turtle()
    brad.color("blue")
    sideLength = 200
    drawTriangle(brad, sideLength)
    if degree > 0:
         range (0,degree):
            drawTriangle(brad, sideLength)
            sideLength = sideLength/2
        sideLength = 200
        brad.forward(sideLength/2)
        brad.right(240)
        brad.forward(sideLength/2)
    window.exitonclick()
drawFractal(4)
