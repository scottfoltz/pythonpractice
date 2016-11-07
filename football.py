from turtle import *
import math
from random import randint



# setup screen size
setup (600, 600, 0, 0)
speed(0)
penup()
goto(-200, 140)
wn = Screen()
wn.bgcolor('#00B200')

yards = 30
#yard markers
for step in range(7):
  write(yards, align='center')
  yards = yards - 5
  right(90)
  left(90)
  forward(50)

goto(-200, 120)
pendown()

#build the field
sideline = 50
for step in range(7):

  color('yellow')
  forward(sideline)
  right(90)
  forward(200)
  right(90)
  forward(sideline)
  right(90)
  forward(200)
  right(90)
  sideline = sideline + 50


redTurtle = Turtle()
redTurtle.color('red')
redTurtle.shape('turtle')

redTurtle.penup()
redTurtle.goto(-150, 20)
print(redTurtle.position())



#screen set up, now we write the game...

#initialize some variables
currentDown = 1
yardsToGo = 10
currentPlayYardage = 0

#infinite loop, until i say so
while(redTurtle.position()[0] <= 100):  
  penup()
  goto(-100,-100)
  #current status.. 
  #i couldnt figure out how to update the numbers in the write function without it overlapping so i just used print
  print('Down ', str(currentDown), ',', str(yardsToGo), ' yards to go.')
  print(redTurtle.position())
  if currentDown <= 4:
    play = input("Pass or Run? (p/r)")
    currentDown = currentDown + 1
    if play == 'r':
        currentPlayYardage = randint(-3,8)
        yardsToGo = yardsToGo - currentPlayYardage
        currentPlayYardage = currentPlayYardage * 10
        print(currentPlayYardage)
        redTurtle.forward(currentPlayYardage)
        print(redTurtle.position()[0])
        continue
    elif play == 'p':
        isComplete = randint(0,1)
        if isComplete == 0: 
          currentPlayYardage = 0
          continue
        else: 
          currentPlayYardage = randint(3,15)
          yardsToGo = yardsToGo - currentPlayYardage
          currentPlayYardage = currentPlayYardage * 10
          print(currentPlayYardage)
          redTurtle.forward(currentPlayYardage)
          print(redTurtle.position()[0])
          continue
    else:
        print('Bad response, try again')
        continue

    #i dont think this works
    if redTurtle.position()[0] >= 100:
        print('You win')
        write('you lose', align='center')
        break
    elif redTurtle.position()[0] >= -50:
      currentDown = 1
      yardsToGo = 10
      continue

    else:
      print('You lose')
      break

  else:
      print('You win')
      write('you lose', align='center')
      break




#get the window to go away on a click
  #exitonclick()

  