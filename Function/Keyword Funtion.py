# Function definition is here
def printme( str1, str2 ):
   "This prints a passed string into this function"
   print ("Mysting1: ", str1)
   print ("Mysting2: ", str2)
   return;

# Now you can call printme function
printme(str1 = "Abdul Wahed", str2= "Ayaan") # whatever we are assigning to the str is a keyword argument without which program will through error
#printme("Abdul Wahed","Ayaan")

# Keyword can be passed in either way as mentioned above

print ('----default Argument----')

def printme( str2, str1= "Sultan"): # non defined argument should be placed first
   "This prints a passed string into this function"
   print ("Mysting1: ", str1)
   print ("Mysting2: ", str2)
   return;

# Now you can call printme function
printme(str2= "Ayaan") # whatever we are assigning to the str is a keyword argument without which program will through error
printme (str1= "change", str2= "Ayaan") # changing the argument