'''
Created on Feb 11, 2018

@author: Kevin
'''
def get_products_of_all_ints_except_at_index(intList):
  if len(intList) < 2:
      raise IndexError('Getting the product of numbers at other '
                       'indices requires at least 2 numbers')
   
  # the output list to hold the products   
  outList = [None] * len(intList)
  
  # For each index, finds all the products before it 
  # and stores the product each iteration
  productSoFar = 1
  for x in range(0, len(intList)):
      outList[x] = productSoFar
      productSoFar *= intList[x]
    
  # For each index, finds all the products after it. 
  # Each index already has the product of all indices
  # before it, so this will yield the final product.
  productSoFar = 1
  for x in range(len(intList)-1, -1, -1):
      outList[x] *= productSoFar
      productSoFar *= intList[x]
      
  return outList
 
list = [1, 2, 3, 4, 5]
list = get_products_of_all_ints_except_at_index(list)
print (list)


  
      
    




    