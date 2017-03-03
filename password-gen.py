import random

print ('**********************************************')
print ('Welcome to the Welcome to the Password Generator!')
print ('**********************************************')

#define an array that will hold all of the words
lineArray = []
passwordArray = []
#prompt user
filename = input('Enter the name of the file to analyze: ')
#read in the file one line at a time without newlines
with open(filename) as my_file:
    lineArray = my_file.read().splitlines()

print(*lineArray)



#we loop based on the value of numPasswords
for i in range(numPasswords):
    #get first word
    word1 = random.choice(wordArray)
    #get second word and capitalize it
    word2 = random.choice(wordArray).upper()
    #get second word
    word3 = random.choice(wordArray)
    #get the random number within respected range
    num = random.randint(1000,9999)

    #find and replace I, S, O in word2
    word2 = word2.replace('I','1')
    word2 = word2.replace('S','$')
    word2 = word2.replace('O','0')

    #concantenate the final string and make sure to change num to a string
    finalPassword = word1 + word2 + word3 + str(num)
    #add that password to our passwordArray
    passwordArray.append(finalPassword)
    

#Here is where we print our results
print('Here are the passwords:')
#using a for loop iterating through our passwords
for i in passwordArray:
    #print each password in the list
    print(i)
