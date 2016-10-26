print "************************************"
print "Welcome to the Paint Cost Calculator"
print "************************************"

#define your givens at the top
doorDimensions = 21*144
windowDimensions = 15*144

#define area per gallon
paintPerGallon = 350*144
primerPerGallon = 200*144

#define the basic dimensions of the room
height = float(input("Please enter the height of the room in inches: "))
length = float(input("Please enter the length of the room in inches: "))
width = float(input("Please enter the width of the room in inches: "))
#surfaceArea = width * length * 2 + width * height * 2 + length * height * 2
surfaceArea = 2 * length * height + 2 * width * height

#yes or no statements
first = raw_input("Is this the first time the room has been painted? (y/n)").lower()
ceiling = raw_input("Do you wish to paint the ceiling? (y/n)").lower()
ceilingArea = length*width
#print "Ceiling Area", ceilingArea

#how many doors and windows
numDoors = float(input("How many doors are there?"))
doorArea = doorDimensions*numDoors
#print "Door Area: ", doorArea

numWindows = float(input("How many windows are there?"))
windowArea = windowDimensions*numWindows
#print"Window Area", windowArea

totalSurfaceArea = surfaceArea - windowArea - doorArea 
withCeiling = int((totalSurfaceArea + ceilingArea) / paintPerGallon) + 1
noCeiling = int(totalSurfaceArea / paintPerGallon) + 1
withPrimer = int(totalSurfaceArea / primerPerGallon) + 1
withPrimerAndCeiling = int((totalSurfaceArea + ceilingArea) / primerPerGallon) + 1
#print "Total SurfaceArea", totalSurfaceArea



#define cost for paint and primer
paintCost = float(input("Enter the cost of paint per gallon: $"))
primerCost = float(input("Enter the cost of primer per gallon: $"))



if first.startswith('n'):
    #print"no primer needed"
    totalPrimer = 0
elif first.startswith('y'):
    if ceiling.startswith('y'):
	    totalPrimer = withPrimerAndCeiling
    else:
        totalPrimer = withPrimer 
else:
    print"Not a valid response"
if ceiling.startswith('n'):
    totalPaint = noCeiling 
elif ceiling.startswith('y'):
    totalPaint =  withCeiling 
else:
    print"Not a valid response"

print "You need to buy", totalPaint, " gallons of paint and ", totalPrimer, "gallons"

totalPaintCost = totalPaint * paintCost
totalPrimerCost = totalPrimer * primerCost

totalCost = totalPaintCost + totalPrimerCost
print"Your total cost will be $", totalCost 
print "Thank you for using Paint Cost Calculator. Good-bye."
