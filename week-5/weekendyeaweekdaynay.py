# Creating a program to respond positively to
# weekend days and negatively to week days.
# Weekday output - Yes, unfortunately today is a weekday.
# Weekend output - It is the weekend, yay!

# References: PandS notes, Whirlwind Tour of Python
# http://anh.cs.luc.edu/handsonPythonTutorial/ifstatements.html


# Create tuple, days of the week.
W = ("Monday", "Tuesday", "Wednesday",
    "Thursday", "Friday", "Saturday", "Sunday")

# Ask user to input a day of the week    
s = input("Input day of week: ")

# outputs depending on user choice of day
if (W[0:4]): 
    print("Yes, unfortunately today is a weekday")  
else: 
    print("It is the weekend, yay!")
