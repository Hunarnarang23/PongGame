from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

tim=Turtle()
tim.color("white")
tim.penup()
tim.goto(0,-290)
tim.hideturtle()
for i in range(0,30):
    tim.setheading(90)
    tim.pendown()
    tim.forward(10)
    tim.penup()
    tim.forward(10)


r_paddle=Paddle((360,0))
l_paddle=Paddle((-360,0))
ball=Ball()
scoreboard=Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")

screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect collision with the wall
    if ball.ycor()> 280 or ball.ycor()<-280:
        #needs to bounce
        ball.bounce_y()
    #detect collision with paddle
    if (ball.distance(r_paddle)<50 and ball.xcor()>320) or (ball.distance(l_paddle)<50 and ball.xcor()<-320):
        ball.bounce_x()


    #detect if ball goes out of Right boundry
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()


    #detect if ball goes out of left boundry
    if ball.xcor() < - 380:
        ball.reset_position()
        scoreboard.r_point()




screen.exitonclick()
