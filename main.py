from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# setup the screen
screen = Screen()
screen.title("Pong")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

# create Paddles, Ball, and Scoreboard.
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


# create Paddle controls.
screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

# game logic
game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.meander()

    # detect collision with upper/lower wall. Bounces ball.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    # detect collision with paddles. Bounces ball.
    if ball.distance(right_paddle) < 40 and ball.xcor() > 320 or ball.distance(left_paddle) < 40 and ball.xcor() < -320:
        ball.paddle_bounce()

    # detect if right paddle misses ball. If so, resets ball. Adds point to scoreboard.
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # detect if left paddle misses ball. If so, resets ball. Adds point to scoreboard.
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
