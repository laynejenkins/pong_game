from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__(shape="square")
        self.penup()
        self.color("white")
        self.speed("slowest")
        self.xmove = 10
        self.ymove = 10
        self.move_speed = 0.1

    def meander(self):
        '''Makes the ball constantly move. Starts moving to upper-right corner.'''
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)

    def wall_bounce(self):
        '''Makes the ball 'bounce' off of upper/lower walls.'''
        self.ymove *= -1

    def paddle_bounce(self):
        '''Makes the ball 'bounce' off of the paddle.'''
        self.xmove *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        '''Once ball hits right/left wall, it resets to middle and heads to opposite player.'''
        self.goto(0, 0)
        self.xmove *= -1
        self.move_speed = 0.1
