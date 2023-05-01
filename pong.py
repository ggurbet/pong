#!/usr/bin/python3.7
# Pong
# Gökhan Gurbetoğlu
# @ggurbet

import turtle
import random
import time

LIGHT = "white"
MEDIUM = "lightgray"
DARK = "dimgray"

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
player1.color(MEDIUM)
player1.penup()
player1.goto(-350, 0)

# Player 2
player2 = turtle.Turtle()
player2.speed(0)
player2.shape("square")
player2.shapesize(stretch_wid = 5, stretch_len = 1)
player2.color(MEDIUM)
player2.penup()
player2.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color(LIGHT)
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1

# Center line
center_line = turtle.Turtle()
center_line.speed(0)
center_line.color("#555555")
center_line.penup()
center_line.goto(0, 400)
center_line.pendown()
center_line.pensize(3)
center_line.setheading(270)
while center_line.ycor() > -400:
    center_line.fd(20)
    center_line.penup()
    center_line.fd(20)
    center_line.pendown()

# Score
score_1 = 0
score_2 = 0

# Scoreboard
score = turtle.Turtle()
score.color(LIGHT)
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("{}  {}".format(score_1, score_2), align="center", font=("Monospace", 24, "normal"))

# Game Over text
game_over = turtle.Turtle()
game_over.color(LIGHT)
game_over.penup()
game_over.hideturtle()
game_over.goto(-10, -240)

# Player Movements
def player1_up():
    y = player1.ycor()
    if y < 240:  # limit the paddle movement within the screen bounds
        y += 50
        player1.sety(y)

def player1_down():
    y = player1.ycor()
    if y > -240:  # limit the paddle movement within the screen bounds
        y -= 50
        player1.sety(y)

def player2_up():
    y = player2.ycor()
    if y < 240:  # limit the paddle movement within the screen bounds
        y += 50
        player2.sety(y)

def player2_down():
    y = player2.ycor()
    if y > -240:  # limit the paddle movement within the screen bounds
        y -= 50
        player2.sety(y)

# Keyboard controls
wn.listen()
wn.onkeypress(player1_up, "w")
wn.onkeypress(player1_down, "s")
wn.onkeypress(player2_up, "Up")
wn.onkeypress(player2_down, "Down")

# Reset game
def reset_game():
    global score_1, score_2
    score_1 = 0
    score_2 = 0
    ball.goto(0, random.randint(-250, 250))
    player1.goto(-350, 0)
    player2.goto(350, 0)
    game_over.clear()
    score.clear()
    score.write("{}  {}".format(score_1, score_2), align="center", font=("Monospace", 24, "normal"))
wn.onkeypress(reset_game, "Return")

# Exit game
def exit_game():
    wn.bye()
wn.onkeypress(exit_game, "q")

# Main loop
while True:
    wn.update()

    # Move the ball
    ball.goto(ball.xcor() + ball.dx, ball.ycor() + ball.dy)

    # Check borders
    if ball.ycor() > 290:
        ball.sety(290) # do not go out of bounds
        ball.dy *= -1 # reverse direction
    if ball.ycor() < -290:
        ball.sety(-290) # do not go out of bounds
        ball.dy *= -1 # reverse direction
    if ball.xcor() > 390:
        score_1 += 1
    if ball.xcor() < -390:
        score_2 += 1
    if ball.xcor() > 390 or ball.xcor() < -390:
        score.clear()
        score.write("{}  {}".format(score_1, score_2), align="center", font=("Monospace", 24, "normal"))
        ball.dx *= -1 # reverse direction
        ball.goto(0, random.randint(-250, 250))
    if ball.xcor() > 360 or ball.xcor() < -360:
        ball.color(DARK)
        turtle.ontimer(lambda: ball.color(LIGHT), 200)

    # Collisions between the ball and the paddles
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < player1.ycor() + 50 and ball.ycor() > player1.ycor() - 50):
        ball.dx *= -1
        ball.setx(-340)
        player1.color(LIGHT)
        turtle.ontimer(lambda: player1.color(MEDIUM), 100)
        player1.shapesize(stretch_wid = 5.5, stretch_len = 1.1)
        turtle.ontimer(lambda: player1.shapesize(stretch_wid = 5, stretch_len = 1), 100)
        ball.shapesize(stretch_wid = 1.5, stretch_len = 1.5)
        turtle.ontimer(lambda: ball.shapesize(stretch_wid = 1, stretch_len = 1), 100)
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < player2.ycor() + 50 and ball.ycor() > player2.ycor() - 50):
        ball.dx *= -1
        ball.setx(340)
        player2.color(LIGHT)
        turtle.ontimer(lambda: player2.color(MEDIUM), 100)
        player2.shapesize(stretch_wid = 5.5, stretch_len = 1.1)
        turtle.ontimer(lambda: player2.shapesize(stretch_wid = 5, stretch_len = 1), 100)
        ball.shapesize(stretch_wid = 1.5, stretch_len = 1.5)
        turtle.ontimer(lambda: ball.shapesize(stretch_wid = 1, stretch_len = 1), 100)

    # Check if game is over
    if score_1 == 5 or score_2 == 5:
        # Stop the ball
        ball.goto(0, -600)

        # Show Game Over screen
        winner = "1" if score_1 > score_2 else "2"
        end_text = "     Player {} wins!\n\nPress Enter to play again\n\n     Press Q to quit".format(winner)

        game_over.write(end_text, align="center", font=("Monospace", 24, "normal"))
        
        wn.update()
        wn.listen()
