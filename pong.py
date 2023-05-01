#!/usr/bin/python3.7
# Pong
# Gökhan Gurbetoğlu
# @ggurbet

import turtle

# Initialize the screen and other objects
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
ball.dx = 0.1
ball.dy = 0.1

# Score
score_1 = 0
score_2 = 0

# Scoreboard
score = turtle.Turtle()
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player 1: {}  Player 2: {}".format(score_1, score_2), align="center", font=("Courier", 24, "normal"))

# Player Movements
def player1_up():
    y = player1.ycor()
    if y < 240:  # limit the paddle movement within the screen bounds
        y += 20
        player1.sety(y)

def player1_down():
    y = player1.ycor()
    if y > -240:  # limit the paddle movement within the screen bounds
        y -= 20
        player1.sety(y)

def player2_up():
    y = player2.ycor()
    if y < 240:  # limit the paddle movement within the screen bounds
        y += 20
        player2.sety(y)

def player2_down():
    y = player2.ycor()
    if y > -240:  # limit the paddle movement within the screen bounds
        y -= 20
        player2.sety(y)

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
        score_1 += 1
        score.clear()
        score.write("Player 1: {}  Player 2: {}".format(score_1, score_2), align="center", font=("Courier", 24, "normal"))
    if ball.xcor() < -390:
        ball.goto(0, 0) # ball is out
        ball.dx *= -1 # reverse direction
        score_2 += 1
        score.clear()
        score.write("Player 1: {}  Player 2: {}".format(score_1, score_2), align="center", font=("Courier", 24, "normal"))

    # Collisions between the ball and the paddles
    if (ball.xcor() > 340 and \
        ball.xcor() < 350) and \
        (ball.ycor() < player2.ycor() + 50 and \
        ball.ycor() > player2.ycor() - 50):
        ball.dx *= -1
        ball.setx(340)
    if (ball.xcor() < -340 and \
        ball.xcor() > -350) and \
        (ball.ycor() < player1.ycor() + 50 and \
        ball.ycor() > player1.ycor() - 50):
        ball.dx *= -1
        ball.setx(-340)
