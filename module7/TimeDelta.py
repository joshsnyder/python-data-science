# This program will utilize datetime library and timedelta module, and print the output for various
# values; current datetime, minus 60 seconds, and add 2 years.
# Joshua Snyder 03/01/2020

from datetime import datetime
from datetime import timedelta

def main():
      Question2()
      print("------------------------------------------")
      Question3()

def Question2():
      # Current datetime
      date = datetime.now()
      # Minus 60 seconds
      subSixtySeconds = date - timedelta(seconds = 60)
      # Add 2 years by number of days
      add2Year = date + timedelta(days = 730)
      print(f"Question #2:\nCurrent datetime: {date}\nMinus 60 seconds: {subSixtySeconds}\nAdd 2 years: {add2Year}")

def Question3():
      # Current datetime
      date = datetime.now()
      # Add 100 days
      oneHundreadDays = date + timedelta(days = 100)
      # Add 10 hours
      tenHours = date + timedelta(hours = 10)
      # Add 13 minutes
      thirteenMinutes = date + timedelta(minutes = 13)
      print(f"Question #3:\nCurrent datetime: {date}\nAdd 100 days: {oneHundreadDays}\nAdd 10 hours: {tenHours}\nAddThirteen minutes: {thirteenMinutes}")

# Execute
main()