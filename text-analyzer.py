from string import punctuation
print ('**********************************************')
print ('Welcome to the Welcome to the Text Analyzer!')
print ('**********************************************')

#define vowels and consonants lists
vowels = list("aeiou")
consonants = list("bcdfghjklmnpqrstvwxyz")

#prompt user
filename = input('Enter the name of the file to analyze: ')

#read in the file
#making all characters lowercase, we do this for when we check for vowels and consonants
with open(filename) as my_file:
    fileContents = my_file.read().lower()

#gets the length of an array of words that are split
words = len(fileContents.split())
#gets all of the occurances of a period
sentences = fileContents.count('.')
#counts the number of lines 
lines = len(fileContents.splitlines())

punctuationCount = 0
#search through fileContents one character at a time
for c in fileContents:
    #then once through 'punctuation' for each c
    for p in punctuation:
        #if theres a match we will increase punctuation by 1
        if c == p:
            punctuationCount += 1


#calculate the sum of the consonants
#for every character in fileContents look to see if theres a match in the consonants list
numConsonants = sum(fileContents.count(c) for c in consonants)
#calculate the sum of the vowels
#for every character in fileContents look to see if theres a match in the vowels list
numVowels = sum(fileContents.count(c) for c in vowels)


#print statementss
print('Results: ')
print('Lines: ', lines)
print('Words:', words)
print('Sentences: ',sentences)
print('Puncuations: ', punctuationCount)
print('Consonants: ', numConsonants)
print('Vowels: ', numVowels)





