def Remove(tuples): 
    tuples = [t for t in tuples if t]
    return tuples 
  
# Driver Code 
tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'),  
          ('krishna', 'akbar', '45'), ('',''),()] 

print(tuples)
print("\n")		  
print(Remove(tuples))


str=" malayalam"
ans=str[::-1]
print(ans)
if ans:
	print("yes")
else:
	print('No')

print("\n****print**")	
s= "Abdul Wahed mohammed"
#s= s.split(' ')

print('Abdul Wahed mohammed', sep='-')

vowels= set("aeiou") # this will make various elements
print(vowels)

s=set({})# empty dictionary will get converted to set
print(type(s))

string="abdulwahed"
print("".join(set(string)))# set will remove the duplicates and ''.join will help to print after removing

print("\n\n** this is to reverse the string ''.join(reversed())")
#''.join(reversed(str) this is to print the str in reverse order
s="malayalam"
rev=''.join(reversed(s))
if s==rev:
	print (True)
else: print(False)

print("\n\n reversing of list")
my_list=[1,2,3,4,5]
print("reversing the elements using reverse keyword:", list(reversed(my_list)))
print("using indexing reversing the list elements:", my_list[::-1])