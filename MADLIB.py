import random
def main():
    print("Welcome to Madlibs! TYPE DIFFERENT WORDS.")
    
name = input("ENTER YOUR NAME: ")
word1 = input("WEIRD PLACE: ")
word2 = input("OCCUPATION: ")

print(str(name) + (" went to the ") + str(word1) + (" to be a ") + str(word2))
if __name__ == "__main__":
    main()