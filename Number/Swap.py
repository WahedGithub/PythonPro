x = input('Enter value of x: ')
y = input('Enter value of y: ')

# create a temporary variable and swap the values
temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))

print("\n\nanother method-1 to swap when positions are known")
def swapPositions(list, pos1, pos2):
	list[pos1], list[pos2]= list[pos2], list[pos1]
	return list
	
list=[21, 34,45, 56]
pos1, pos2= 1,3

print(swapPositions(list, pos1-1,pos2-1))

print("\n\nanother method-3 to swap when positions are UN-known")
def swapList(newList): 
    #size = len(newList) 
      
    # Swapping  
    temp = newList[0] 
    newList[-1] = temp 
    newList[0] = newList[-1] 
      
    return newList 
      
# Driver code 
newList = [12, 35, 9, 56, 24] 
  
print(swapList(newList)) 

print("\n\nanother method-4 using indexing to swap when positions are UN-known")
def swapList(newList): 
      
    newList[0], newList[-1] = newList[-1], newList[0] 
  
    return newList 
      
# Driver code 
newList = [12, 35, 9, 56, 24] 
print(swapList(newList)) 