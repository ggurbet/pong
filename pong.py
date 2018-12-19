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

# Main loop
while True:
    wn.update()