from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move_ball(self):
        newX = self.xcor()+self.x_move
        newY = self.ycor()+self.y_move
        self.goto(newX, newY)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def ball_reset(self):
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.bounce_x()

    def inc_speed(self):
        if self.x_move < 0:
            self.x_move *= -1
            self.x_move += 1
            self.x_move *= -1
        else:
            self.x_move += 1

        if self.y_move < 0:
            self.y_move *= -1
            self.y_move += 1
            self.y_move *= -1
        else:
            self.y_move += 1

    def speed(self):
        return (self.x_move, self.y_move)
