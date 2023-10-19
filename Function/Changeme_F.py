# Function definition is here
def changeme( mylist ): 
	"This changes a passed list into this function"
	mylist= ([1,2,3,4])
	mylist.append([1,2,3,4]) # add the value to the list and note append don't need to assign the value(=)
	print ("Values inside the function: ", mylist)
	return
# Now you can call changeme function
mylist = [10,20,30]
changeme( mylist ) # function can b called directly without print function
print ("Values outside the function: ", mylist)