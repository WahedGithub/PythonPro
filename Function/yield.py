# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print (str)
   #return (str);

printme("ABDUL\n")

#print("\n********this is with YIELD*******")
def printme():
   yield 1
   yield 1
   yield 3
   
for value in printme():
  print(value)
  

print ("""\n\nReturn sends a specified value back to its caller whereas Yield can produce a sequence 
of values. We should use yield 
when we want to iterate over a sequence, but don’t want to store the entire sequence in memory.""")


print ("""\n\n  A Python program to generate squares from 1 to 100 using yield 
and therefore generator""")
def square():
	i =1
	while True:
		yield i*i
		i+=1

for num in square():
	if num > 100:
		break
	print(num)
	

print("""\n\nWAP for yield and lambda""")	
def cube(y):
	return y*y*y
	
g= lambda x: x*x*x
print(g(5))

print(cube(5))