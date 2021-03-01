from sys import argv 

script, filename = argv 
# it just opens a text file 
txt = open(filename)
# it tells the console a function and prints it out
print(f"Here's your file (filename):")
print(txt.read())

input(> )