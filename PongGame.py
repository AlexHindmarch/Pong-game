import turtle
import time
import random

# Set up the window
win = turtle.Screen()
win.title("Pong Game")
win.bgcolor("black")
win.setup(width=600, height=400)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=3, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-270, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=3, stretch_len=1)
paddle_b.penup()
paddle_b.goto(270, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 4  # Initial x-speed (adjust as needed)
ball.dy = -4  # Initial y-speed (adjust as needed)

# Paddle movement functions
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
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

# Function to update paddle positions
def update_paddles():
    # Check if the window is still open
    if win.window_width() > 0 and win.window_height() > 0:
        win.update()
        win.ontimer(update_paddles, 5)  # Update every 20 milliseconds

# Start updating paddle positions
update_paddles()

# Game Over turtle
game_over_turtle = turtle.Turtle()
game_over_turtle.speed(0)
game_over_turtle.color("white")
game_over_turtle.penup()
game_over_turtle.hideturtle()
game_over_turtle.goto(0, 0)

# List of Game Over messages
game_over_messages = [
    "Game Over - I dare you to try again!",
    "Oops! Game Over!",
    "Game Over - Think you can do better? Prove it!",
    "My mum can do better :p",
    "Good effort but not good enough! - Game Over!"
]

# List of User Win messages
user_win_messages = [
    "Congratulations! You Win!",
    "Amazing! You're the Pong Champion!",
    "Victory is yours! Well done!",
    "You conquered Pong! What's next?",
    "You're unbeatable! You Win!"
]


# Function to display Game Over message
def display_game_over(user_wins=False):
    game_over_turtle.clear()  # Clear previous messages
    if user_wins == True:
        selected_message = random.choice(user_win_messages)
    else:
        selected_message = random.choice(game_over_messages)
    game_over_turtle.write(selected_message, align="center", font=("Arial", 24, "normal"))
    time.sleep(2)  # Wait for 2 seconds
    game_over_turtle.clear()  # Clear the message

# Function to control the AI for Paddle A
def ai_control():
    # Introduce randomness to occasionally miss the ball
    random_number = random.randint(1, 7)
    if random_number == 1:
        # Randomly miss the ball
        if ball.xcor() < -100 and ball.dx < 0:
            if paddle_a.ycor() < ball.ycor():
                paddle_a_down()
            elif paddle_a.ycor() > ball.ycor():
                paddle_a_up()
    else:
        # Follow the ball
        if ball.xcor() < -100 and ball.dx < 0:
            if paddle_a.ycor() < ball.ycor():
                paddle_a_up()
            elif paddle_a.ycor() > ball.ycor():
                paddle_a_down()

# Main game loop
start_time = time.time()
user_wins = False  # Initialize user_wins to False 

while True:
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 190 or ball.ycor() < -190:
        ball.dy *= -1

    # Paddle and ball collisions
    if (ball.xcor() > 240 and ball.xcor() < 250) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.color("blue")
        ball.setx(240)
        ball.dx *= -1

    elif (ball.xcor() < -240 and ball.xcor() > -250) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.color("red")
        ball.setx(-240)
        ball.dx *= -1

    # AI control for Paddle A
    ai_control()

    # Check if the ball has gone off-screen
    # Check if the ball has gone off-screen
    if ball.xcor() < -win.window_width() / 2:
        user_wins = True
        display_game_over(user_wins)
        ball.goto(0, 0)
        ball.dx *= -1  # Reverse the direction
    elif ball.xcor() > win.window_width() / 2:
        user_wins = False
        display_game_over(user_wins)
        ball.goto(0, 0)
        ball.dx *= -1  # Reverse the direction

        # Optional: Reset other game elements as needed
        # paddle_a.goto(-400, 0)
        # paddle_b.goto(400, 0)

    # Speed up every 10 seconds
    elapsed_time = time.time() - start_time
    if elapsed_time > 10:
        ball.dx *= 1.1  # Increase x-speed by 10%
        ball.dy *= 1.1  # Increase y-speed by 10%
        start_time = time.time()

# Close the turtle graphics window when clicked
win.exitonclick()