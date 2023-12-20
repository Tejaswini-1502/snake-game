from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# setting up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# creating the snake
snake = Snake()

# initializing the food
food = Food()

# controlling the snake
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)


# move the snake
game_is_on = True
score_board = Scoreboard()
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    # detect the collision of the snake with the food
    # dimension of the food 10x10 (keeping extra 5 as buffer)
    if snake.head.distance(food) < 15: # snake.head.distance(food) is the distance of the first segment of the snake from the food
        # tracking the user's score
        score_board.update_score()

        # food needs to go to a new random location
        food.refresh()

        # extending the body of the snake
        snake.extend()

    # detecting collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score_board.game_over()

    # detecting collision with the tail
    # if the head of the snake collides with any segment in the tail then trigger game over

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score_board.game_over()

screen.exitonclick()