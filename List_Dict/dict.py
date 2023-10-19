dict = {'Nam e': 'Zara', 'Age': 7, 'Class': 'First'}; # {Key: Value}
dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School"; # Add new entry
print ("dict['Age']: ", dict["Age"])
print ("dict['School']: ", dict['School'])
print (dict)
print('points---duplicates keys are not allowed but values are allowed but old value will get replaced with new value')
print('order not applicable')
# Built in dictionary method
# [has_key]:
#print ("---searching for particular key----")
#if (dict.has_key['Nam e']):
	#print ("there is a key Nam e in the dict")
#else:
#	print ("there is no key with Name in the dict")


print ("\n---deleting an element from dict----")
del dict['Nam e']; # deletes the element from the dict
#if (dict.has_key['Nam e']):
#	print ("there is a key Nam e in the dict")
#else:
#	print ("there is no key with Name in the dict")
	

print (dict.keys()) # prints the available keys
print (dict.values()) # prints the available values

print("\nBefore clearing the dict:", dict)

dict.clear(); # will clear all the available elements under the dict

print("\nafter clearing the dict:", dict)

dic= {1:'abdul', 'name': 'wahed', 2: 'mohd'}
print (dic)

print("\nusing dic[key]:", dic['name'])

print("\nusing get:", dic.get(1))# this is used for printing if the interger values as saved as key

