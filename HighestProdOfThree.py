'''
Created on Feb 12, 2018

@author: Kevin
'''

def getHighestProdOfThree(int_list):
    # sort list into ascending order
    int_list.sort()
    
    # highest product must be either the three highest numbers
    # OR the two lowest and the one highest
    prodThreeHighest = int_list[-1]*int_list[-2]*int_list[-3]
    prodTwoLowOneHigh = int_list[0]*int_list[1]*int_list[-1]
    
    # find and return the max of these two options
    highestProd = max(prodThreeHighest, prodTwoLowOneHigh)
    
    return highestProd
    
int_list = [3, -10, 2, 1, -10]
print("Highest product of three items in list: %d" % getHighestProdOfThree(int_list))