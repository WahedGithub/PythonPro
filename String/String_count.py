#!/usr/bin/python

var1 = 'Hello World!'
var2 = "Python Programming"

#build in string methods
# str.count('alphabet') gives the count of that particular 

print (var1.count('o'))
print (var1.count('l'))
print (var2.count('P'))

print ("------Striping line------")

#string.rstrip() removes the last character/space, deletes multiple characters/spaces until the last character/space
str = "This is test "
print (str.rstrip()) # This removes the space at the end

str = "This is test"
print (str.rstrip())

#('Skillset: Support of validation activities for Connected Car and eCall features.

#Able to build and modify test rigs, support crash-test and laboratory certification activities

#record and analyse test results

#prepare vehicles and ECUs for test by use of CAN and Ethernet diagnostic tools.

#Ability to use vehicle loggers and MAL ticketing tools (Mantis and Jira).



#Deliverables: Support all validation activities across eCall, Stolen Vehicle Tracking, and OTA software update features.


#t')) # This removed the char(t) at the end, single or multiple characters(same will get removed)

print ("------Spliting line------")


print (str.split()) # returns a list with 3 elements note: if nothing is given than space will be taken as delimiter
print (str.split(' is ')) # returns a list with 2 elements (whatever is given in the bracket will be deleted

