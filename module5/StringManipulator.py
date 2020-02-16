# This program will accept a string input, insert it into the middle of another string using
# string interpolation. This manipulated string is then returned to the user.
# Joshua Snyder 02/16/2020

def main():
    stringManipulator(input('Enter string value: '))

def stringManipulator(inputString):
    return print((f'This is a string manipulated by your input: {inputString}, congratulations on manipulating a string.'))

# Execute program
main()
