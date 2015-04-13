import turtle
import random

def draw_square(some_turtle):
    for i in range(0,4):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("white")
    #creating brad
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(100)
    for i in range(0,72):
        draw_square(brad)
        brad.right(5)
    #angie's our circle turtle
    #angie = turtle.Turtle()
    #angie.shape("arrow")
    #angie.color("purple")
    #angie.circle(100)

    window.exitonclick()


draw_art()
