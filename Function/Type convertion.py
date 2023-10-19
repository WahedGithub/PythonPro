print("####Converting float to int#####")
a= 10.5690 #float object
print(int(a)) #this will convert the float value to int numbers after decimal

print("####Converting int to float#####")
a=10
print(float(a))

print("####Converting complex to int#####")
#int(10+20j) #can't convert complex value to Int

print("####Converting bool to int#####")
print(int(True)) # returns 1

print(int(False)) # returns 0

print(bool(10))# returns true
print(bool(0))#returns false
print(bool(0.00001))#returns true if its not zero then it will be always true

print('str to int')
print(int('15')) # string internally contains only intergal value & base-10

print(int('0b1111'))# returns error

print(int(10.5))# returns error

print('Converting bool from string)
print(bool('True'))#returns True
print(bool('False'))#returns True
print(bool('Yes'))#returns True
print(bool('no'))#returns True
print(bool(''))#returns false only for empty string it returns false

a= 10
b= 10
print(id(a)) #gives id else u can use "a is b" to check if the objects are same or not



