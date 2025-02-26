from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor('black')
screen.title("THE PONG")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-359, 0))
ball = Ball((0,0))
score = Score()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect the collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # bounce
        ball.bounce_y()

    #detect the collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #detect r paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    #detect l paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

    screen.update()




screen.exitonclick()
