friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s = [friend for friend in friends if friend.startswith("S")]


print(friends)
print(starts_s)
print(friends is starts_s)
print("friends: ", id(friends), "start_s:", id(starts_s))

