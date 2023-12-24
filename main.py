from random import randint


def generate_random_number():
    random_num = randint(1,100)
    return random_num


def calculate(user_guess):
    global number_of_attempts, win_or_lose
    if user_guess != generated_num:
        number_of_attempts -= 1
        if user_guess > generated_num:
            print("Too high.")
        else:
            print("Too low.")
    else:
        number_of_attempts = 0
        print(f"You guessed a right number - {user_guess}")
        win_or_lose = True


print("Welcome to the number Guessing Game!\n")
print("I am thinking of a number between 1 and 100.")
difficulty = ''
while difficulty not in ['easy', 'hard']:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard' :  ").lower()
if difficulty == 'easy':
    number_of_attempts = 10
else:
    number_of_attempts = 5

generated_num = generate_random_number()
win_or_lose = False

while number_of_attempts > 0:
    while True:
        try:
            guess = int(input("Make a guess: "))
            break
        except ValueError:
            print("Enter a valid number.")
    calculate(guess)
    if number_of_attempts > 0:
        print(f"You have {number_of_attempts} attempts remaining to guess the number.")

if win_or_lose:
    print("You won!")
else:
    print(f"You lost, the right number was {generated_num}")


