import turtle
import direction
import random
import time
running = True

def display():
    fullBody = []
    delay = 0.1
    score = 0
    screen = turtle.Screen()
    screen.title("The Snake Game")
    screen.setup(width = 700, height = 700)
    screen.tracer(0)
    turtle.bgcolor("turquoise")
    turtle.speed(5)
    turtle.pensize(4)
    turtle.penup()
    turtle.goto(-310,250)
    turtle.pendown()
    turtle.color("black")
    turtle.forward(600)
    turtle.right(90)
    turtle.forward(500)
    turtle.right(90)
    turtle.forward(600)
    turtle.right(90)
    turtle.forward(500)
    turtle.penup()

    snake = turtle.Turtle()
    snake.speed(0)
    snake.shape("square")
    snake.color("black")
    snake.penup()
    snake.goto(0,0)
    snake.direction = "stop"

    fruit = turtle.Turtle()
    fruit.speed(0)
    fruit.shape('circle')
    fruit.color('red')
    fruit.penup()
    fruit.goto(30,30)

    scoring = turtle.Turtle()
    scoring.speed(0)
    scoring.color("black")
    scoring.penup()
    scoring.hideturtle()
    scoring.goto(0,300)
    scoring.write("Score :",align="center",font=("Courier",24,"bold"))

    def turnUp():
        if snake.direction != "down":
            snake.direction = "up"

    def turnDown():
        if snake.direction != "up":
            snake.direction = "down"

    def turnLeft():
        if snake.direction != "right":
            snake.direction = "left"

    def turnRight():
        if snake.direction != "left":
            snake.direction = "right"

    def exitGame():
        global running
        running = False
        screen.bye()

    screen.listen()
    screen.onkeypress(exitGame, "Escape")
    screen.onkeypress(turnUp, "Up")
    screen.onkeypress(turnDown, "Down")
    screen.onkeypress(turnLeft, "Left")
    screen.onkeypress(turnRight, "Right")

    while running:
        screen.update()
        if snake.distance(fruit)< 20:
            x = random.randint(-290,270)
            y = random.randint(-240,240)
            for chunk in fullBody:
                if chunk.distance(fruit) < 20:
                    x = random.randint(-290,270)
                    y = random.randint(-240,240)
            fruit.goto(x,y)
            scoring.clear()
            score+=1
            scoring.write("Score:{}".format(score),align="center",font=("Courier",24,"bold"))
            delay-=0.001
            
            body = turtle.Turtle()
            body.speed(0)
            body.shape('square')
            body.color('red')
            body.penup()
            fullBody.append(body)
        if running:
            for index in range(len(fullBody)-1,0,-1):
                a = fullBody[index-1].xcor()
                b = fullBody[index-1].ycor()
                fullBody[index].goto(a,b)

            if len(fullBody)>0:
                    a= snake.xcor()
                    b = snake.ycor()
                    fullBody[0].goto(a,b)

        direction.snakeMove(snake, running)

        if snake.xcor()>280 or snake.xcor()< -300 or snake.ycor()>240 or snake.ycor()<-240:
            time.sleep(1)
            screen.clear()
            screen.bgcolor('turquoise')
            scoring.goto(0,0)
            scoring.write("   GAME OVER \n Your Score is {}".format(score),align="center",font=("Courier",30,"bold"))
            time.sleep(3)
            break
        for chunk in fullBody:
            if chunk.distance(snake) < 20:
                time.sleep(1)
                screen.clear()
                screen.bgcolor('turquoise')
                scoring.goto(0,0)
                scoring.write("    GAME OVER \n Your Score is {}".format(score),align="center",font=("Courier",30,"bold"))
                time.sleep(3)
                break
        time.sleep(delay)