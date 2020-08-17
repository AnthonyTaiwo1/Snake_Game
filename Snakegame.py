import turtle # good for making simple games
import time
import random
import winsound
import playsound

delay= 0.1


# Score
score = 0
high_score = 0

# window specification
win= turtle.Screen()
win.title("Snake Game by Anthony Taiwo")
win.bgcolor("blue")
win.setup(width=600, height=600)
win.tracer(0)               #turns off animation of the sreen


# snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction="stop"

# snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

bodyparts= []


# pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score:0", align="center", font=("courier",24,"normal"))


# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
     if head.direction != "up":
         head.direction = "down"

def go_right():
     if head.direction != "left":
         head.direction = "right"

def go_left():
     if head.direction != "right":
         head.direction = "left"        

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)        

#keyboard binding
win.listen()
win.onkeypress(go_up, "w")  
win.onkeypress(go_down, "s")  
win.onkeypress(go_right, "d")  
win.onkeypress(go_left, "a")     
   
#main game loop
while True:
    win.update()

    # check for a collision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction= "stop"

        # Hide the bodyparts
        for bodypart in bodyparts:
            bodypart.goto(1000,1000)

        # clear the bodyparts list
        bodyparts.clear() 

        # Reset the score
        score = 0 

        #update score display
        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score,high_score),align="center", font=("courier",24,"normal"))  
    
    # check for a collision with the food
    if head.distance(food) < 20:
        # Move food to a different part of the screen
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)


        # Add a bodypart
        new_bodypart = turtle.Turtle()
        new_bodypart.speed(0)
        new_bodypart.shape("circle")
        new_bodypart.color("black")
        new_bodypart.penup()
        bodyparts.append(new_bodypart)

        # shorten the delay
        delay -= 0.001

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score,high_score),align="center", font=("courier",24,"normal"))    

    


    # move the end bodyparts first in reverse order
    for index in range(len(bodyparts)-1,0,-1):    # length of segments x starts from 0 to x-1, going to go down to zero. this would stop at 1. so it would go down from x to + 1.
        x = bodyparts[index-1].xcor()
        y = bodyparts[index-1].ycor()  
        bodyparts[index].goto(x, y) 

    # move bodypart 0 to where the head is
    if len(bodyparts) > 0:
        x = head.xcor()
        y = head.ycor()
        bodyparts[0].goto(x,y)    


    move()

    # check for head collision with the rest of the body
    for bodypart in bodyparts:
        if bodypart.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            # Hide the bodyparts
            for bodypart in bodyparts:
                bodypart.goto(1000, 1000)

            # clear the bodyparts list
            bodyparts.clear()

            # Reset the score
            score = 0 

            # reset the delay
            delay = 0.1

            #update score display
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score,high_score),align="center", font=("courier",24,"normal"))     



    time.sleep(delay)

win.mainloop()    
