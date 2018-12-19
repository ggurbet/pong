#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Pong
# Gökhan Gurbetoğlu
# @ggurbet

import turtle

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("#282c34")
wn.setup(width = 800, height = 800)
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

# Main loop
while True:
    wn.update()