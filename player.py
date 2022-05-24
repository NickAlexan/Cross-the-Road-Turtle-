from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black", "green")
        self.penup()
        self.setheading(90)
        self.go_to_start()


    def go_to_start(self):
        self.goto(0, -230)

    def go_up(self):
        self.forward(20)

    def go_down(self):
        self.backward(20)

