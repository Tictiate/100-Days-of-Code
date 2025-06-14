from operator import index
import art
import random
print("Lets play BlackJack!!")
print(art.logo)

cards = [11, 2, 3, 4, 5 ,6 ,7, 8, 9, 10, 10, 10, 10]

while True:
    userCards = []
    computerCards = []

    userCards.append(random.choice(cards))
    userCards.append(random.choice(cards))
    computerCards.append(random.choice(cards))

    print(f"\tYour cards: {userCards}, current score: {sum(userCards)}")
    print(f"\tComputer's first card: {computerCards[0]}")

    def finalSimulation():
        while sum(computerCards) < 17:
            computerCards.append(random.choice(cards))
        print(f"\tYour final hand: {userCards}, final score: {sum(userCards)}")
        print(f"\tComputer's final hand: {computerCards}, final score: {sum(computerCards)}")


    hit = True
    while hit:
        ask = input("Type 'y' to get another card, type 'n' to pass: ")
        if ask == "y":
            userCards.append(random.choice(cards))
            print(f"\tYour cards: {userCards}, current score: {sum(userCards)}")
            if 11 in userCards and sum(userCards) > 21:
                userCards[index(11)] = 1
            elif sum(userCards) == 21 :
                print("BLACKJACK!")
                finalSimulation()
                hit = False
            elif sum(userCards) > 21:
                print("BUST.")
                finalSimulation()
                hit = False
            print(f"\tComputer's first card: {computerCards[0]}")
            if sum(computerCards) > 21:
                print("Computer BUSTed.")
        else:
            finalSimulation()
            hit = False

    if (sum(userCards) > 21 and sum(computerCards) > 21) or (sum(userCards) == sum(computerCards)):
        print("Draw. 😰")
    elif (sum(userCards) <= 21 and sum(computerCards) > 21) or (sum(userCards) > sum(computerCards) and sum(userCards) <= 21):
        if sum(userCards) == 21:
            print("You have BlackJack!")
        print("You Win! 🤩")
    else:
        if sum(computerCards) == 21:
            print("Computer has BlackJack!")
        print("You Lose! 🤯")

    playAgain = input("Do you want to play again? y/n: ")
    if playAgain == "n":
        break
    else:
        print("\n"*100)
        print(art.logo)
