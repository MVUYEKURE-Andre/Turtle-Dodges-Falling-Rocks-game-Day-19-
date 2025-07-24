from turtle import Turtle
class Player(Turtle):
    def __init__(self):
        super().__init__()
        # self.color("black")
        self.shape("turtle")
        self.penup()
        self.goto(0, -250)
        self.left(90)

    def go_right(self):
        new_x = self.xcor() + 10
        self.goto(new_x, self.ycor())

    def go_left(self):
        new_x = self.xcor() - 10
        self.goto(new_x, self.ycor())


