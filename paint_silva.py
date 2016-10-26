print "************************************"
print "Welcome to the Paint Cost Calculator"
print "************************************"

#define the door and window dimensions
doorDimensions = 21*144
windowDimensions = 15*144

#define area per gallon
paintPerGallon = 350*144
primerPerGallon = 200*144

#define the basic dimensions of the room
height = float(input("Please enter the height of the room in inches: "))
length = float(input("Please enter the length of the room in inches: "))
width = float(input("Please enter the width of the room in inches: "))

#simple equation to comput the Surface Area of the walls
surfaceArea = 2 * length * height + 2 * width * height

#yes or no statements that turns given input into lowercase
first = raw_input("Is this the first time the room has been painted? (y/n)").lower()
ceiling = raw_input("Do you wish to paint the ceiling? (y/n)").lower()
ceilingArea = length*width

#how many doors and windows
numDoors = float(input("How many doors are there?"))
doorArea = doorDimensions*numDoors

numWindows = float(input("How many windows are there?"))
windowArea = windowDimensions*numWindows


#get the total Surface Area assuming there wasnt a ceiling added
totalSurfaceArea = surfaceArea - windowArea - doorArea 
#gets the cost of paint with the ceiling included
withCeiling = int((totalSurfaceArea + ceilingArea) / paintPerGallon) + 1
#gets the cost of paint without the ceiling included
noCeiling = int(totalSurfaceArea / paintPerGallon) + 1
#cost of primer
withPrimer = int(totalSurfaceArea / primerPerGallon) + 1
#cost of primer with the ceiling
withPrimerAndCeiling = int((totalSurfaceArea + ceilingArea) / primerPerGallon) + 1
#print "Total SurfaceArea", totalSurfaceArea


#define cost for paint and primer
paintCost = float(input("Enter the cost of paint per gallon: $"))
primerCost = float(input("Enter the cost of primer per gallon: $"))

#if the first letter of the input for first time is an 'n'
if first.startswith('n'):
    totalPrimer = 0
#if this is the first time
elif first.startswith('y'):
	#and you want the ceiling painted
    if ceiling.startswith('y'):
	    totalPrimer = withPrimerAndCeiling
	#if not
    else:
        totalPrimer = withPrimer 
#if the input was not a 'n' or a 'y' return error message
else:
    print"Not a valid response"

#if the customer did not want to include the ceiling
#we set totalPaint to appropriate variable
if ceiling.startswith('n'):
    totalPaint = noCeiling 
elif ceiling.startswith('y'):
    totalPaint =  withCeiling 
else:
    print"Not a valid response"

#Here is the output statements showing the correct amount of paint to buy
print "You need to buy", totalPaint, " gallons of paint and ", totalPrimer, "gallons"

#cost calculations
totalPaintCost = totalPaint * paintCost
totalPrimerCost = totalPrimer * primerCost

totalCost = totalPaintCost + totalPrimerCost

#output of the total cost and good-bye
print"Your total cost will be $", totalCost 
print "Thank you for using Paint Cost Calculator. Good-bye."
