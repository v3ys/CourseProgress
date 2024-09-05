from art import logo, vs
from game_data import data
import random

def  person_data(person):
    person_name = person["name"]
    person_desc = person["description"]
    person_country = person["country"]
    return f"{person_name} a {person_desc} from {person_country}"

def checker(guess, person_1, person_2):
    if guess == "a" and (person_1["follower_count"] > person_2["follower_count"]):
        return True
    elif guess == "b" and (person_1["follower_count"] < person_2["follower_count"]):
        return True
    else:
        return False


print(logo)
score = 0
game_status = True

person_2 = random.choice(data)

while game_status:
    person_1 = person_2
    person_2 = random.choice(data)
    if person_1 == person_2:
        person_2 = random.choice(data)
    print(f"Compare A: {person_data(person_1)}.")
    print(vs)
    print(f"Against B: {person_data(person_2)}.")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    print("\n" * 20)
    print(logo)
    answer = checker(guess, person_1, person_2)
    if answer:
        score += 1
        print(f"You're right! Current score {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        game_status = False
