# Should we import the users? or should i just make a better security thing


username = []
password = []
user_name = input("Welcome, what is your name? ")
user_password = input("Please type in your password. ")

print(f"Thank you {user_name}, welcome back!")

if user_name in user_name:
    username.append(user_name)
    print("Username has been stored.")

if user_password in user_password:
    password.append(user_password)
    print("Password has been stored.")

show_password = input("Would you like to see your password? type Y or N: ")

yes = "y"
no = "n"

if yes in show_password:
    print(user_password)
if no in show_password:
    print("Password will not be shown") 