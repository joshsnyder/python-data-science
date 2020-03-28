# This program is a simple example utilizing the matplotlib module to create an example line chart
# Joshua Snyder - 03/28/2020

import matplotlib.pyplot as plt

# Global variables
x = ["Jan", "Feb", "Mar", "Apr" ," May", "Jun"]
y = [10.00, 10.15, 11.28, 15.00, 15.12, 16.00]
xLabel = "Month"
yLabel = "Dollars"
chartTitle = "Silver Spot Average \n (2019)"

def main():
    plt.plot(x, y)
    plt.ylabel(yLabel)
    plt.xlabel(xLabel)
    plt.title(chartTitle)
    plt.grid(True)
    plt.annotate('Incredible spike!', xy=('Mar',11.25), xytext=('Apr', 12.775), arrowprops = dict(facecolor='black', shrink=0.02))
    plt.annotate('Incredible spike!', xy=('Apr',15), xytext=('Apr', 12.775), arrowprops = dict(facecolor='black', shrink=0.02))
    plt.show()

# Execute program
main()