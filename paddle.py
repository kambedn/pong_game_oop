from turtle import Turtle
UP = 90
DOWN = 270
DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, x_pos, upkey, downkey):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.speed("fastest")
        self.penup()
        self.goto(x_pos, 0)
        self.upkey = upkey
        self.downkey = downkey
        self.setheading(UP)
        self.turtlesize(1, 5, 2)

    def move_up(self):
        self.setheading(UP)
        self.forward(DISTANCE)

    def move_down(self):
        self.setheading(DOWN)
        self.forward(DISTANCE)

    def reset_position(self, x_pos):
        self.goto(x_pos, 0)


