import turtle

#Create a canvas distance
myturtle = turtle.Turtle()

#Go to a certain coordinate
myturtle.penup()
myturtle.goto(50,75)

myturtle.pendown()
myturtle.forward(100) # move 100 pixels
myturtle.left(90) #turn 90 degrees
myturtle.forward(200)
myturtle.left(90)
myturtle.forward(100)
myturtle.left(90)
myturtle.forward(200)

turtle.done()