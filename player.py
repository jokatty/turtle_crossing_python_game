from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)
        self.restart = False

    def move(self):
        self.forward(MOVE_DISTANCE)
        if self.ycor() >= FINISH_LINE:
            self.goto(STARTING_POSITION)
            self.restart = True
