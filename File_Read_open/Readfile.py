#str= raw_input("Enter the Input:")
#print str

# Open a file
fo = open(("foo.txt"), "r")
s = fo.read()
print ("Stuff from the foo.txt file is :", s)

#close opened file
fo.close()

print("\n*******Method-2**********")
print(open('foo.txt').read())


print("\n*******Method-3 Using For Loop**********")
file = open('foo.txt','r')
for each in file:
	print(each)

	
print("\n*******Method-4 Character wise**********")
f=open('foo.txt', 'r')
print(f.read(4)) # this will print the first four characters