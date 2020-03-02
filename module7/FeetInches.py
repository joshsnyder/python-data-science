# This program will accept two arguments (feet and inches)
# Joshua Snyder 03/01/2020

from datetime import datetime
feet = 2
inches = 6
date = datetime.now()

def main(feet, inches, date):
    print(f"Current datetime: {date}\nInput argument feet: {feet}\nInput argument inches: {inches}")

# Execute
main(feet, inches, date)