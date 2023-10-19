class MyClass:
	"This is my second class"
	a = 10
	def func(self):
		print('Hello')

# Output: 10
print("instance variable", MyClass.a)

# Output: <function MyClass.func at 0x0000000003079BF8>
print("Method", MyClass.func)

# Output: 'This is my second class'
print(MyClass.__doc__)

ob= MyClass() # creating the object for class
ob.func() # calling the function
print(ob.func()) # this will return none as already print function is mentioned in the method