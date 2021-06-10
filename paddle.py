

from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        # turtles are 20x20, stretchwidth 20x5=100, paddle is 20x100
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(position)
    
    def go_up(self):
        if self.ycor() < 250:
            new_y = self.ycor() + 20
            self.goto(self.xcor(),new_y)
        else:
            # limiter so paddles don't go off screen
            self.goto(self.xcor(), 250)
    
    def go_down(self):
        if self.ycor() > -250:
            new_y = self.ycor() - 20
            self.goto(self.xcor(),new_y)
        else:
            # limiter so paddles don't go off screen
            self.goto(self.xcor(), -250)
