import  random

guess_numer = random.randint(1, 50)
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count = guess_count + 1
    if guess == guess_numer:
        print("Oh wow you won")
        break
else:
    print("You lose")
