import random

def guessing_game():
    "Random Numbers!"

    print("Im thinking of. a number between 1 and 10.")

    number = random.randint(1, 10)
    attempts = 3

    while True:
        try:
            user_guess = int(input("Enter your guess:"))
            attempts += 1

            if user_guess < number:
                print("Too low, try again!")
            elif user_guess > number:
                print("Too high, try again!")
            else:
                print(f"Congrats, you guessed right. The number is {number} in {attempts} attempts!") 
                break

        except ValueError:
            print("Incorret! try againg, the right answer was {number}.")

if __name__ == "__main__":
    guessing_game()