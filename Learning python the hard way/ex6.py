types_of_people = 10 # you are setting up a variables and a value
x = f"There are {types_of_people} types of people." # Formating a variable to basically plug in anywhere

binary = "binary" #its basically doing the most with the least amount of typing... format laziness ftw
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}." # plugging in the format. do not forget the f in the beginning

print(x) # printing the variable so we dont have to type it all again
print(y)

print(f"I said; '{x}'") # simply saves time by plugging in the (x) variable you are printing the text and variable
print(f"I also said; '{y}'") # Do Not forget the f at the beginning for functions

hilarious = True
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e) # combines both strings, but you can also manioulate which side its on
