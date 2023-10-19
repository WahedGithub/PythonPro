Str = input("Enter the small letters input:")
print("capital Letters: ", Str.upper())

##lowercase
Str = input("Enter the capital letter input:")
print("Small Letters: ", Str.lower())

s = 'durga'
output = s[0].upper()+s[1:]
print(output) # returns first character as capital

output = s[0:len(s)-1]+s[-1].upper()
print(output)# returns last character as capital

output= s[0].upper()+ s[1:len(s)-1]+ s[-1].upper()
print(output)#returns First & Last character as capital

