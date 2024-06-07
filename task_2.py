# Design an INDIAN FLAG using python turtle

import turtle

def draw_rectangle(color, x, y, width, height):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

def draw_ashoka_chakra(radius):
    turtle.penup()
    turtle.goto(0, -radius)
    turtle.pendown()
    turtle.color("navy")
    turtle.width(2)
    turtle.circle(radius)
    
    # Draw 24 spokes
    for _ in range(24):
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        turtle.forward(radius)
        turtle.backward(radius)
        turtle.right(15)

def draw_indian_flag():
    turtle.speed(3)
    turtle.bgcolor("white")
    
    # Dimensions of the flag
    flag_height = 300
    flag_width = 450
    stripe_height = flag_height / 3

    # Draw the saffron stripe
    draw_rectangle("orange", -flag_width / 2, flag_height / 2, flag_width, stripe_height)

    # Draw the green stripe
    draw_rectangle("green", -flag_width / 2, -flag_height / 2, flag_width, stripe_height)

    # Draw the Ashoka Chakra in the center
    draw_ashoka_chakra(stripe_height / 2)

    turtle.hideturtle()
    turtle.done()

draw_indian_flag()
