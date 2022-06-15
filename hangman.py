import random
import time

def guessTheWord():
    wordsList = "head arm back waist leg face chest stomach hip hand foot eye \
eyebrow nose mouth chin hair ear lips neck nail thumb finger wrist palm \
shoulder elbow knee forehead cheek teeth tongue brain"

    wordsList = wordsList.split(" ")
    chosenWord = wordsList[int(random.random()*len(wordsList))]
    chances = len(chosenWord) + 2
    guessList = []

    print("Guess the word! HINT: The word is a body part :)")
    word = ["_"]*len(chosenWord)
    print(" ".join(word))
    print("Enter a letter: ")

    start = time.time()
    while chances > 0:
        guess = input()

        if not guess.isalpha():
            print("ERROR! Please enter a letter.")
            continue
        elif len(guess) > 1:
            print("Please enter a single character.")
            continue
        elif guess in guessList:
            print("You already entered that letter.")
            continue
    
        guessList.append(guess)
        if guess in chosenWord:
            for i in range (len(chosenWord)):
                if chosenWord[i] == guess:
                    word[i] = guess
                else:
                    continue
            print(" ".join(word))
    
        else:
            chances -= 1
            print(" ".join(word))
    
        for i in range (len(chosenWord)):
            if chosenWord[i] == word[i]:
                if i == len(chosenWord) -1:
                    print("Congrats! You found the word.")
                    end = time.time()
                    print("Elapsed time is {}".format(end-start))
                    endGame()
            else:
                break                 
            
        if chances == 0:
            print("Game Over! The word was: " + chosenWord)
            end = time.time()
            print("Elapsed time is {}".format(end-start))
            endGame()
    
def endGame():
    print("Enter 'yes' for another round, 'no' to exit the game")
    answer = input()

    while answer not in ["YES", "NO"]:
        if answer.upper() == "YES":
            guessTheWord()
        elif answer.upper() == "NO":
            exit()
        else:
            print("Please enter a valid answer.")
            print("Enter 'yes' for another round, 'no' to exit the game")
            answer = input()

guessTheWord()
    
