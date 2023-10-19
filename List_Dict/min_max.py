list= []
list.append(5)
list.extend([2,3,4])
list.insert(0,20)
print("after extend + append",list)

print("\n\n*******WAP")
print("The list is ",list) 
  
# Assign first element s a minimum. 
min = list[0] 
  
for i in range(len(list)): 
  
    # If the other element is min than first element 
    if list[i] < min:  
        min = list[i] #It will change
print("The smallest element in the list is ",min) 


