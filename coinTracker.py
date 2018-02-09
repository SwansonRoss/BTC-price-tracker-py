# Program that automatically tracks the price of bitcoin in USD
# and returns today's price and the 30 day high.
#
# Uses dursk's bitcoin price API to pull data:  https://github.com/dursk/bitcoin-price-api

from decimal import Decimal
from exchanges.bitfinex import Bitfinex
import requests
import time

# Takes in a list and a new price then adds the price to the end of the list.
# If the list has 30 items in it, all items are shifted down one position and
# the new price is added to the end of the list.
def addMostRecent(list, price):
    if len(list) < 30:
        list.append(price)
    else:
        for i in range (0, 29, 1):
            list[i] = list[i+1]
        list[29] = price
    return list

# Takes in a list, loops through to average the sum
def avgPrice(list):
    sum = 0
    for i in range (0, len(list), 1):
        sum = sum+list[i]
    avg = sum/(len(list))
    return avg

# Calls API to update current price
def checkPrice():
    newPrice = Bitfinex().get_current_price()
    return newPrice

# Takes in a list and returns the high price
def findHighestPrice(list):
    list.sort(reverse=True)
    return list[0]

# Takes in a list, prints out a list of prices, then prints the average
def printList(list):
    print "Price:"
    for i in range (0, len(list), 1):
        print "  - $" + str('{:.2f}'.format(list[i]))
    print "30 day average: $" + str('{:.2f}'.format(avgPrice(list)))
    print "30 day high: $" + str('{:.2f}'.format(findHighestPrice(list)))+"\n"

#TODO: Class to hold summary of last 30 days
#   - list with last 30 days prices
#   - Current price
#   - High price
#   - Days at highest price
#class past30:
#    def __init__(self, price, days):
#        self.prices = []
#        self.current = current
#        self.highPrice = highPrice
#        self.days = days

currPrice = checkPrice()

print str(currPrice) + " at " + time.asctime( time.localtime(time.time()) )

listHr = list(range(0,5))
listDay = []

#TODO: figure out keypress events, loop until keypress
for j in range (0, 40, 1):      # Replace with while loop
    for i in range (0, 5, 1):   # Range should be (0, 24, 1)
        listHr[i] = checkPrice()
        #time.sleep(60*60)
        time.sleep(5) #For testing
    hrPrice = avgPrice(listHr)
    print "Daily average at "+ time.asctime( time.localtime(time.time())) + ": " + str('{:.2f}'.format(hrPrice)) + "\n"

    listDay = addMostRecent(listDay, hrPrice)

printList(listDay)
