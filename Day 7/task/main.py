import random
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo

lives = 6

print(logo)

chosen_word = random.choice(word_list)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
guessed_letters = []

while not game_over:
    print("****************************" + f"{lives}" +"/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You have already guessed [" + guess + "]")
        continue
    else:
        guessed_letters.append(guess)

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        print("[" + guess + "] is not in the word. You lose a life.")
        lives -= 1

        if lives == 0:
            game_over = True
            print("The word was: " + chosen_word)
            print(f"***********************YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])
