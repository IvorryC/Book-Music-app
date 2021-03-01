formatter = "{} {} {} {}" # you create a string of 4 places and format it
# below you print the sring and the fromat, your formatter tells the console where to put it... call it an argument
print(formatter . format(1, 2, 3, 4))
print(formatter . format("one", "two", "three", "four"))
print(formatter . format(True, False, False, True))
print(formatter . format(formatter, formatter, formatter, formatter))
print(formatter . format(
    "Set free",
    "To numbed leaves",
    "The dead Tree",
    "Is now free"
))
