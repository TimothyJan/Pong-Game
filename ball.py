
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 15
        self.y_move = 15
        self.move_speed = 0.1 # use with time.sleep

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    
    def bounce_y(self):
        self.y_move *= -1
    
    def bounce_x_right(self):
        self.x_move *= -(abs(self.x_move))
        self.move_speed *= 0.9
    
    def bounce_x_left(self):
        self.x_move *= abs(self.x_move)
        self.move_speed *= 0.9       
    
    def reset_position(self, direction):
        self.goto(0,0)
        self.move_speed = 0.1 # reset ball move_speed
        # change direction when one side wins
        if direction == "right":
            self.bounce_x_left()
        elif direction == "left":
            self.bounce_x_right()
