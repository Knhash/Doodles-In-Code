import turtle
import math

#Initialization
screen=turtle.Screen()
screen.bgcolor("#000000")
initial=turtle.Turtle()
initial.hideturtle() 
initial.shape("turtle")
initial.color("#FFFFFF")
initial.penup()
initial.setx(0)
initial.sety(0)
initial.pendown()   
distance = 0

def square_spiral():
    global initial
    global distance

    #Make it colorful
    colors = ['blue', 'white', 'green', 'white']

    turnSum = 0
    length = 5
    displacement = -0.5
    drawSpeed = 0
    setAngle = 60 
    #Spiral Out
    for i in range(0,1000):
        initial.color(colors[i % len(colors)])
        distance = math.sqrt((length * length) + (displacement * displacement))
        turnAngle = math.atan(displacement/length)
        turnAngle = math.degrees(turnAngle)
        turnSum = turnSum + turnAngle
        print turnSum
        if turnSum < -(135+360):
            break
        initial.forward(distance)
        initial.right(setAngle+turnAngle)
        initial.speed(drawSpeed)
        length = length - displacement

def start():
    square_spiral()
    screen.exitonclick()

start()
