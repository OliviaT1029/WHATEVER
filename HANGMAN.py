import random
def main():
    print("Welcome to HANGMAN! Guess the letter to spell the word.")
    answer ='SPAGHETTI'  
    length = len(answer)
    tries = 10
    print("The answer is a " + str(length) + " letter word.")
    display_string = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
    while (tries > 0):
        print("You have " + str(tries) + " tries left")
        guess = input("Guess a letter: ")
        
        if guess.upper() in answer:
            print("Correct")
            for i in range(length):
                if answer[i] == guess:
                    display_string[i] = guess
                
            print(display_string)
        else:
            print("Try Again")
            tries = tries - 1
        
            
    if tries == 0:
        print("You lose! The answer was " + answer)
if __name__ == "__main__":
    main()