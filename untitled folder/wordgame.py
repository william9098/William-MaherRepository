import random, os
os.system('cls')

def updateWord(word, guesses):
    correctCount = 0
    for letter in word:
        if letter in guesses:
            print(letter, end=" ")
            correctCount += 1
        else:
            print('_', end= " ")
    if correctCount == len(word):
        return True
    else:
        return False

def Menu():
    print()
    print("###############################")
    print("The goal is to guess a word from a category, the categories are provided below")
    print("#          MENU        #")
    print(                                 )
    print("           1. Animals          ")
    print("           2. Computer Parts         ")
    print("           3. Fruits         ")
    print("           4. Scoreboard        ")
    print("           5. Exit          ")
    print()
    print("############################")
    print("#    To play the game select 1-3       #")
    print("#       To exit select 5              #")
    sel=input("What would you like to do? ")
    sel=int(sel)
    return sel

def updateScoreFile():
    myFile= open('score.txt', 'a')
    myFile.write(name + "\t Highest score:\t"+str(maxScore))
    myFile.write("\n")
    myFile.close()

def endGame():
    updateScoreFile()
    os._exit(0)

def sel4():
    myFile= open('score.txt', 'r')
    print(myFile.read())
    myFile.close()
    sel = Menu()
    return sel

def wordSelection():
    if sel == 1:
        word = random.choice(animals)
    if sel == 2:
        word = random.choice(compParts)
    if sel == 3:
        word = random.choice(fruits)
    return word

animals=["tiger", "elephant"]
fruits=["banana", "strawberries"]
compParts=["keyboard", "Monitors", "computer","trackpad", "case","Operating System"]
name= input("What is your name? ")
maxScore = 0

sel = Menu()

while sel!=0:

    if sel==5:
        print("Goodbye!")
        endGame()
    elif sel==4:
        sel = sel4()
    elif sel==1 or sel==2 or sel==3:
        word = wordSelection()
        word = word.lower()
        wordCount = len(word)
        turns = wordCount+2
        score = 0
        print(name + ", Good Luck! You have", turns, "chances to guess my word.")
        guesses = '' 
        correctGuess = False
        updateWord(word, guesses)
        while correctGuess== False and turns > 0:
            print()
            newguess=input("Give me a letter: ")
            newguess= newguess.lower()
            if newguess in word:
                guesses += newguess
                print("You guessed one letter. ")
            else:
                turns -= 1
                print("\n You have ", turns, " turns left.")
            correctGuess = updateWord(word, guesses) 
        
        if correctGuess == False:
            print("You are out of turns!")
        
        score = 3*wordCount + 5*turns
        if score > maxScore:
            maxScore = score
        answer = input("\n Would you like to return to menu? y/n ")
        if ('y' in answer):
            sel = Menu()
        else:
            sel = 0
    else:
        endGame()

endGame()