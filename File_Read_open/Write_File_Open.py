str=  input("Enter the Input:")
print (str)

print('Creating a file and writing data into it')
fo = open("f.txt", "w")
fo.write("Python is a Scripting Langugage\n Yeah its a great Langugage!!\n");
#print str

fo.close() #close opened file

print(open('f.txt').read()) # prints the written file


# Python code to illustrate append() mode 
file = open('f.txt','a') 
file.write("This will add this line") 
file.close() 

print( "after appending the line:", open('f.txt').read()) # prints the written file