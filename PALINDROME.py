def main():
    print("Palindromes!")
    word = input("Enter a word:")
    i = 0
    j = len(word)-1
    palindrome = False
    while word[i] == word[j] and i<len(word)-1 and j>0:   
        i = i+1
        j = j-1
        palindrome = True
        
    if palindrome == True:
        print(word + " is a palindrome.")
    elif palindrome == False:
        print(word + " is not a palindrome.")
    

if __name__ == "__main__":
    main()