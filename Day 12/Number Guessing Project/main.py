logo = '''   ___                       _____ _                __                 _               
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|   
                                                                                       '''
import random

answer = random.randint(1,100)
print(answer)

def initGame():
    lives = 0
    print(logo)
    print("Welcome to the Number Guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    gameMode = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if gameMode == "easy":
        lives = 10
    elif gameMode == "hard":
        lives = 5
    else:
        print("Please enter valid input")
        initGame()
    return lives

def game():
    global lives
    print(f"You have {lives} attempts to guess the number.")
    while lives > 0:
        guess = int(input("Make a guess:"))
        if answer > guess:
            print("Too low.\nGuess again")
            lives -= 1
        elif answer < guess:
            print("Too high.\nGuess again")
            lives -= 1
        else:
            print(f"You got it! The answer was {answer}")
            break
    if lives < 1:
        print(f"You lost. The number was: {answer}")

gameOn = True
while gameOn:
    lives = initGame()
    game()
    playAgain = input("Do you want to play again? Type 'yes' or 'no': ")
    if playAgain == "no":
        gameOn = False