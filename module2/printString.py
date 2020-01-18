# Module 2 utilizing a variable, string and print functions to output that varible to the console
# Joshua Snyder 01/18/2020

import string
# Set variable to static string text and print before manipulation
output = 'Testing the ability to set a variable to a string and utilize the print function to output this variable to the console'
print("Before manipulation via string function:")
print(output)
print() # space for readability

# Now we'll utilize the string function to manupulate our string variable in various formats
print("After manipulation via string function methods")
# All uppercase
print("Uppercase: " + str.upper(output))
# All lowercase
print("Lowercase: " + str.lower(output))
# Title case
print("Title case: " + str.title(output))

