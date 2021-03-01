number = 7
user_input = input("Enter 'y' if you'd like to play: ").lower()

if user_input == "y":
    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("Well done")
    elif abs(number - user_number) == 1:
        print("You were off by one.") 
    else:
        print("You Fool.")