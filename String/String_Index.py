#!/usr/bin/python

var1 = 'Hello World!'
var2 = "Python Programming"

print('slicing of String')
print (var1[:])

print ("var2:", 'Hello ' + var2[:19])# returns string from 0 to 18

print ("var2[1:5]: is ", var2[1:5]) #returns string from 1 to 4

print ("var2[5:1]: is ", var2[5:1])# returns empty as it wont go in reverse order

print ("var1[:end]: is ", var1[:-1])# if nothing is given it will take from 0

print ("var1[Begin:]: is ", var1[0:])

# To print the statement in reverse
print ("Reverse Var1:", " is " + var1[::-1])

print (var1[:99])# slice operator never going to raise index error so it will print till last word.