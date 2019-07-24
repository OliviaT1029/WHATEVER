def main():
    answ=input("What color do you prefer? (Pink or Black) ").lower()
    if answ == ("black"):
        print("You will die alone. Bye!")
    elif answ == ("pink"):
        answ2=input("Where would you choose to go on vacation? (Antartica or Europe) ").lower()
        if answ2 == ("antartica"):
            print("You will die alone. Bye!")
        elif answ2 == ("europe"):
                answ3=input("How many kids do you want? (0,1,2,2+) " )
                if answ3 == ("0"):
                    print("You will die alone. Bye!")
                else :
                    answ4=input("What is your favourite season? (Winter, Summer, Fall or Spring) ").lower()
                    if answ4 == ("winter"):
                        print("You will die alone. Bye!")
                    elif answ4 == ("summer"):
                        print("You will die alone. Bye!")
                    elif answ4 == ("fall"):
                        print("You will die alone. Bye!")
                    elif answ4 == ("spring"):
                        print("You will not die alone and will have children to surround you with a pink house in Europe in Spring. Bye!")
if __name__ == "__main__":
    main()