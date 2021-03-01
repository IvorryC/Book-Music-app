from sys import argv
program, player_one, player_two = argv

print("The game is", program)

print("You are the First Player", player_one)
player_one = input("State thy Name. ")
weapon_1 = input("And your weapon of choice. ") 

print("You are the Second player", player_two)
player_two = input("And Your Name? ")
weapon_2 = input("And your weapon of choice? ")

print(f"So you are {player_one}, and your weapon is {weapon_1} and you are {player_two}, and the weapon you chose is a {weapon_2}. let's begin")
