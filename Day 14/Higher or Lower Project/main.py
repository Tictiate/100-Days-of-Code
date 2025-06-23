import random
from game_data import data
import art

correct = True
score = 0
person1 = random.choice(data)
person2 = random.choice(data)


def display():
    print(art.logo)
    print(f"Compare A: {name1}, a {des1}, from {country1}")
    print(f"Followers: {followers1}M")
    print(art.vs)
    print(f"Compare B: {name2}, a {des2}, from {country2}")

def check(ask):
    global score, correct
    if ask == "a" or "A":
        if followers1 >= followers2:
            score += 1
            print("\n" * 100)
            print(f"You're right! Current score: {score}")
        else:
            print("\n" * 100)
            print(art.logo)
            print(f"Sorry, that's wrong. Final Score: {score}")
            correct = False
    elif ask == "b" or "B":
        if followers2 >= followers1:
            score += 1
            print("\n" * 100)
            print(f"You're right! Current score: {score}")
        else:
            print("\n" * 100)
            print(art.logo)
            print(f"Sorry, that's wrong. Final Score: {score}")
            correct = False


while correct:
        person1 = person2
        name1 = person1["name"]
        des1 = person1["description"]
        country1 = person1["country"]
        followers1 = person1["follower_count"]
        person2 = random.choice(data)
        name2 = person2["name"]
        des2 = person2["description"]
        country2 = person2["country"]
        followers2 = person2["follower_count"]
        display()
        ask = input("Who has more followers? Type 'A' or 'B': ")
        check(ask)