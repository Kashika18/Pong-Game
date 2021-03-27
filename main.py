import turtle


wn = turtle.Screen()
wn.title("Pong by Kashika")
wn.bgcolor("blue")
wn.setup(width=800, height=600)
wn.tracer(0) #stops window from updating and we do it manually which makes the game faster


#input user names
player1 = turtle.textinput("Enter your Name","Player 1")
player2 = turtle.textinput("Enter your Name","Player 2")

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(10)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(10)
paddle_b.shape("square")
paddle_b.color("black")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = .5
ball.dy = .5

# Pen
pen = turtle.Turtle() #turle is the module name and Turtle is the class name
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("{}: 0  {}: 0".format(player1,player2),
          align="center",
          font=("Courier", 24, "normal"))


# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update() #every time the loop runs, the screen is updated

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking

    # Top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 #reverses the direction
        

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        

    # Left and right
    if ball.xcor() > 350:
        score_a += 1
        pen.clear()
        pen.write("{}: {}  {}: {}".format(player1,score_a,player2, score_b),
                  align="center",
                  font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -350:
        score_b += 1
        pen.clear()
        pen.write("{}: {}  {}: {}".format(player1,score_a,player2, score_b),
                  align="center",
                  font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle and ball collisions
    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor(
    ) > paddle_a.ycor() - 50:
        ball.dx *= -1
        

    elif ball.xcor() > 340 and ball.ycor(
    ) < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
        
