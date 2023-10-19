def f1():
	print("this is simple global variable:", s)
	
s = "this is Global variable"
print("Global variables are the one that are defined and declared outside a function and we need to use them inside a function.")
f1()

def f():
    global s 
    print(s) 
    s = "Look for Geeksforgeeks Python Section"
    print(s)  
  
# Global Scope 
s = "Python is great!" 
f() 
#print(s)


print("\nExamples illustrating First Class functions in Python")
e =f
e()