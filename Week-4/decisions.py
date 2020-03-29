# use statements to create a program to manipulate integers
# if a positive even integer is entered / by 2
# if a positive odd integer is entered x by 3 and + 1
# break when you get to 1
# I had completed this weeks ago using notes and Whirlwind Tour of Python



f = input ("a positive integer (1 to quit): ")
f = int(f)
print (f)
while (f > 1): 
    if f % 2 == 0: f = (f / 2)
    else: f = (f*3+1)
    print (f)
