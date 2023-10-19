list1 = [1,4,9,12,16,0,9,8,5,6]
list2 = [0,5,9,13,17,34,42]
list3 = [1,4,9]

print("Gives the length of the list")
print(len(list1))
print('\nGives the sum of the list')
print(sum(list3))

#Need to check for multiplication


#print(product(list3))

print ("\n--------average of the list-------") #getting the average of the list
list = [10,20,30]
tot = sum(list)#list[0] + list[1] + list[2]
listlen= len(list)
avg = tot/listlen

print ("Average value is: ", avg)

print ('\n---append---')#append the element at last position of the list
list4= [123, 'abc', 35, 'wahed']
list4.append('abdul') #append the element at last position of the list
print ("Updated list: ", list4)

print (" \n------inserting the value to the list-------")

#insert(index, "value")
list4.insert(2, 'yes')
print ("Updated insert list: ", list4)
 
print (" \n------removing the value from the list-------")

#insert(index, "value")
print (" the list before removal" ,list4)
list4.remove('yes')
print ("\nUpdated insert list: ", list4)

print (" \n--reverse the elements---")
list4.reverse()
print (" \nlist after reversal:", list4)

