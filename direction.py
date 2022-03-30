import random

def snakeMove(snake, boo):
    if boo:
        if snake.direction == "up":
            y = snake.ycor()
            return snake.sety(y + 20)
        if snake.direction == "down":
            y = snake.ycor()
            return snake.sety(y - 20)
        if snake.direction == "left":
            x = snake.xcor()
            return snake.setx(x - 20)
        if snake.direction == "right":
            x = snake.xcor()
            return snake.setx(x + 20)