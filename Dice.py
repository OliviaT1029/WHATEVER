import random
def main():
    print("Welcome to dice! Guess the number rolled on the die between 1 and 6.")
    answer = random.randint(1,6)
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
        print("You lose! The answer was " + str(random.randint(1,6)))
if __name__ == "__main__":
    main()