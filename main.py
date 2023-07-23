from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")  # changing screen background colour
screen.title("Snake Game")
screen.tracer(0)  # turning tracer off, only after using update(), the screen refreshes the picture
screen.addshape("coffee.gif")

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.go_up, key="Up")
screen.onkey(fun=snake.go_down, key="Down")
screen.onkey(fun=snake.go_left, key="Left")
screen.onkey(fun=snake.go_right, key="Right")

game_is_on = True
while game_is_on:
    screen.update()  # screen updates after all three segments moved
    time.sleep(0.1)  # delay of 1 second after all segments moved
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 17:
        food.reposition()
        snake.grow_snake()
        scoreboard.update_score()

    # Detect collision with wall
    if snake.hits_the_wall():
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:  # we excluded snake head
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
