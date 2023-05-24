from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score, HalfLine
import time

TIME = 0.015  # defines the speed of the ball
BREAK_TIME = 1.0
PADDLE_STARTING_X_COR = 350

# creating screen
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.tracer(0)
screen.title("Pong")

# creating paddles
paddle_left = Paddle(x_pos=-PADDLE_STARTING_X_COR, upkey="w", downkey="s")
paddle_right = Paddle(x_pos=PADDLE_STARTING_X_COR, upkey="Up", downkey="Down")

# creating the ball
ball = Ball()

# creating the half line
half_coords = [y for y in range(290, -291, -40)]
half_line = [HalfLine(y) for y in half_coords]

# making screen listen to clicking/pressing keys
screen.listen()
# the game can be played by two players
# the first players uses Up and Down keys, whilst the other uses W and S keys
screen.onkeypress(paddle_left.move_up, paddle_left.upkey)
screen.onkeypress(paddle_right.move_up, paddle_right.upkey)
screen.onkeypress(paddle_left.move_down, paddle_left.downkey)
screen.onkeypress(paddle_right.move_down, paddle_right.downkey)

# Creating Score
score_right = Score(x_pos=35)
score_left = Score(x_pos=-35)

# game loop
winner = ""
game_is_on = True
while game_is_on:

    screen.update()
    time.sleep(TIME)  # using time sleep so that every object on the screen moves smoothly

    ball.move()  # moving the ball

    # detecting collision with a wall
    if abs(ball.ycor()) > 290:
        ball.bounce_wall()

    # detecting collision with a paddle
    if 340 <= abs(ball.xcor()) <= 350 and (ball.distance(paddle_right) < 50 or ball.distance(paddle_left) < 50):
        ball.bounce_paddle()

    # checking if one of the players scored
    if abs(ball.xcor()) > 380:
        if ball.xcor() > 0:
            score_left.increase_score()
            if score_left.is_winner():  # ending the game
                game_is_on = False
                winner = "left"
                score_left.write_game_over("left")
        else:
            score_right.increase_score()
            if score_right.is_winner():  # ending the game
                game_is_on = False
                winner = "right"
                score_right.write_game_over("right")

        # resetting paddles to their starting positions
        paddle_left.reset_position(-PADDLE_STARTING_X_COR)
        paddle_right.reset_position(PADDLE_STARTING_X_COR)

        # If one of the players scores a point, the ball goes to (0,0) and starts moving into different direction
        # there is also a short break

        ball.reset_position()
        time.sleep(BREAK_TIME)

screen.exitonclick()
