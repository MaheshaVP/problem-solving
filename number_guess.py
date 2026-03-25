#guess the number

import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num,highest_num)

guesses = 0
is_running = True

print("Python number guessing game")
print(f"select the number between {lowest_num} and {highest_num} : ")

while is_running:
    guess = input("Enter your guess : ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num and guess > highest_num:
            print("The number is out of range")
            print(f"please select the number between {lowest_num} and {highest_num} : ")

        elif guess < answer:
            print("Too low! try again")
        elif guess > answer:
            print("Too high! try again")
        else:
            print(f"correct the answer is {answer}")
            print(f"number of guesses is : {guesses}")
            is_running = False

    else:
        print("Invalid guess")
        print(f"please select the number between {lowest_num} and {highest_num} : ")

