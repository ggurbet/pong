#!/usr/bin/python3.7
# Pong
# Gökhan Gurbetoğlu
# @ggurbet

import turtle

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("#282c34")
wn.setup(width = 800, height = 600)
wn.tracer(0)

# Player 1
player1 = turtle.Turtle()
player1.speed(0)
player1.shape("square")
player1.shapesize(stretch_wid = 5, stretch_len = 1)
player1.color("#e9e9e9")
player1.penup()
player1.goto(-350, 0)

# Player 2
player2 = turtle.Turtle()
player2.speed(0)
player2.shape("square")
player2.shapesize(stretch_wid = 5, stretch_len = 1)
player2.color("#e9e9e9")
player2.penup()
player2.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("#e9e9e9")
ball.penup()
ball.goto(0, 0)
ball.dx = 2 # each move is 2 pixels horizontally
ball.dy = 2 # each move is 2 pixels vertically
# combined effect is diagonal 2x2 movement

# Player Movements
def player1_up():
    y = player1.ycor()
    y += 20
    player1.sety(y)

def player1_down():
    y = player1.ycor()
    y -= 20
    player1.sety(y)

def player2_up():
    y = player2.ycor()
    y += 20
    player2.sety(y)

def player2_down():
    y = player2.ycor()
    y -= 20
    player2.sety(y)

# Ball movement


# Keyboard controls
wn.listen()
wn.onkeypress(player1_up, "w")
wn.onkeypress(player1_down, "s")
wn.onkeypress(player2_up, "Up")
wn.onkeypress(player2_down, "Down")

# Main loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Check borders
    if ball.ycor() > 290:
        ball.sety(290) # do not go out of bounds
        ball.dy *= -1 # reverse direction
    if ball.ycor() < -290:
        ball.sety(-290) # do not go out of bounds
        ball.dy *= -1 # reverse direction
    if ball.xcor() > 390:
        ball.goto(0, 0) # ball is out
        ball.dx *= -1 # reverse direction
    if ball.xcor() < -390:
        ball.goto(0, 0) # ball is out
        ball.dx *= -1 # reverse direction