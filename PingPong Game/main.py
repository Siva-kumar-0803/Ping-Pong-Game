from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
s = Screen()
s.setup(800, 600)
s.bgcolor("black")
s.title("PingPong")
s.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


s.listen()
s.onkey(l_paddle.go_up, "w")
s.onkey(l_paddle.go_down, "s")
s.onkey(r_paddle.go_up, "Up")
s.onkey(r_paddle.go_down, "Down")
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    s.update()
    ball.moving()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and (ball.xcor() > 320) or ball.distance(l_paddle) < 50 and (ball.xcor() < -320):
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
s.exitonclick()