import random
def main():
    print("Welcome to random number guesser! Guess the number between 1 and 100.")
    answer = random.randint(1,100)
    tries = 4
    while (tries > 0):
        guess = int(input("Guess a number: "))
        if answer == guess:
            print("Correct")
        else:
            if guess > answer:
                print("Your guess was too high!")
            else:
                print("Your guess was too low!")
            tries = tries - 1
            print("You have " + str(tries) + " tries left")
    if tries == 0:
        print("You lose! The answer was " + str(random.randint(1,100)))
if __name__ == "__main__":
    main()