import turtle
from random import randint,randrange

#prompt user for names of turtles
redTurtleName = input("Enter the name of the red Turtle: ")
greenTurtleName = input("Enter the name of the green Turtle: ")


#read in the file
filename = input("Enter name of file: ")
file_var = open(filename,"r")
#create a separate array for the x and y values
redX,redY = [],[]
for line in file_var:
    #split every time theres a space in the line
    line = line.split()
    #append the first element to xarray
    redX.append(line[0])
    #append the second element to y array
    redY.append(line[1])

file_var.close()
#print(redX)
#print(redY)

# setup screen size
turtle.setup (1000, 1000, 0, 0)
#draw the boundary square
boundaryTurtle = turtle.Turtle()
boundaryTurtle.penup()
boundaryTurtle.goto (-400, 400)
boundaryTurtle.pendown()
boundaryTurtle.forward(800)
boundaryTurtle.left(90)
boundaryTurtle.forward(-800)
boundaryTurtle.left(90)
boundaryTurtle.forward(800)
boundaryTurtle.left(90)
boundaryTurtle.forward(-800)
boundaryTurtle.left(90)


#create the red turtle, put it in its position and spin it to face the right
redTurtle = turtle.Turtle()
redTurtle.color('red')
redTurtle.shape('turtle')

redTurtle.penup()
redTurtle.goto(-400, 200)
redTurtle.pendown()

for turn in range(10):
  redTurtle.right(36)

#create the green turtle, put it in its position and spin it to face the right
greenTurtle = turtle.Turtle()
greenTurtle.shape('turtle')
greenTurtle.color('green')

greenTurtle.penup()
greenTurtle.goto(-400, -200)
greenTurtle.pendown()

for turn in range(60):
  greenTurtle.right(6)



i = 0
#get current position of green
gX = greenTurtle.position()[0]
gY = greenTurtle.position()[1]
while(greenTurtle.position()[0] < 400 and redTurtle.position()[0] < 400):

  #give red turtle next set of coordinates
  redTurtle.goto(float(redX[i]),float(redY[i]))

  #get the next coordinate randomly for green turtle
  gX = greenTurtle.position()[0] + randint(1,20)
  gY = greenTurtle.position()[1] + randint(-5,5)
  #get the green turtle to move to those random points
  greenTurtle.goto(float(gX),float(gY))
  #increment loop
  i = i + 1

#print statements to see who wins
if redTurtle.position()[0] > greenTurtle.position()[0]:
  print(redTurtleName, "Wins!")
  turtle.write (redTurtleName + ' Wins!', font = ('Arial', 36, 'bold'))


elif redTurtle.position()[0] == greenTurtle.position()[0]:
  print("We have a tie")
  turtle.write ('We have a tie', font = ('Arial', 36, 'bold'))

else:
  print(greenTurtleName, "Wins!")
  turtle.write (greenTurtleName + ' Wins!', font = ('Arial', 36, 'bold'))



#get the window to go away on a click
turtle.exitonclick()

  