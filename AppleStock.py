'''
Created on Feb 11, 2018

@author: Kevin
'''
# not done

# Given a list of yesterday's stock prices with index corresponding to minutes after trading opened
# this function finds the maximum profit that could've been achieved by buying/selling at the right times
def get_max_profit(prices):
    
    if len(prices) < 2:
        raise ValueError('Getting a profit requires at least 2 prices')
    
    # Initiate max price and max profit variables
    # These will be updated greedily as we work backward through the list of prices
    maxPrice = prices[-1]
    maxProfit = prices[1]-prices[0]
    
    # Works backward through list of prices
    # For each new price it checks the profit using the maxPrice found so far
    # Updates maxPrice as it goes
    for x in range(len(prices)-2, -1, -1):
        if (maxPrice - prices[x] > maxProfit):
                maxProfit = maxPrice - prices[x]
        if (prices[x] > maxPrice):
            maxPrice = prices[x]
    
    return maxProfit

#stock_prices_yesterday = [10, 7, 12, 5, 8, 11, 9]
stock_prices_yesterday = [4, 16, 10, 6, 1]
print('Max profit yesterday: $%d' % get_max_profit(stock_prices_yesterday))


