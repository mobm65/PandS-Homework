# Write a program to count the number of times
#the letter e appears in a file.
# The program takes its filename argument from the command line.
# Import 'system' functionality

import sys 

# Use the special 'sys.argv' list to access 
# the values passed in from the command line
filename = sys.argv[1]

f = open(filename, "r")

poem = ""

for line in f:
    poem += line

print(poem.count("e"))

f.close()
