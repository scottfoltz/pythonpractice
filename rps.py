from random import choice

print ('**********************************************')
print ('Welcome to the Welcome to Rock Paper Scissors!')
print ('**********************************************')

#create a list for the possibilities 
rps = ['0','1','2']
playerScore = 0
cpuScore = 0


while 1:
    #get the users input
    user = input('Enter 0 for Rock, 1 for Paper, 2 for Scissors: ')
    #randomize the computer choice by giving it only the options from list
    cpu = choice(rps);

    #this is where we test each case and keep a running sum of each score
    if user == cpu:
        print ('Its a draw. Nobody won that round.')
    elif user == '0' and cpu == '2':
        print ('Rock busts scissors. You won that round!')
        playerScore += 1
    elif user == '0' and cpu == '1':
        print ('Paper covers Rock. Computer won that round')
        cpuScore += 1
    elif user == '2' and cpu == '1':
        print ('Scissors cuts Paper. You won that round!')
        playerScore += 1
    elif user == '2' and cpu == '0':
        print ('Rock busts scissors. Computer won that round')
        cpuScore += 1
    elif user == '1' and cpu == '2':
        print ('Scissors cuts Paper. Computer won that round')
        cpuScore += 1
    elif user == '2' and cpu == '2':
        print ('Paper covers rock. You won that round!')
        playerScore += 1



    #if the player reached 3 wins before the cpu reached 3 player wins
    if playerScore == 3 and cpuScore < 3:
        print('You won ', playerScore, 'to', cpuScore)
        break
    #if the cpu reached 3 wins before the player reached 3 cpu wins
    elif cpuScore == 3 and playerScore < 3:
        print('Sorry, computer won ', cpuScore, 'to', playerScore)
        break
    #if the cpu reached 4 wins before the player reached 4 cpu wins
    elif cpuScore == 4 and playerScore <= 3:
        print('Sorry, computer won ', cpuScore, 'to', playerScore)
        break
    #if the player reached 4 wins before the cpu reached 4 player wins
    elif playerScore == 4 and cpuScore <= 3:
        print('You won ', playerScore, 'to', cpuScore)
        break


