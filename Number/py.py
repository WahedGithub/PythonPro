print("\n\n******WAP to palindrome with method-1***********")

def ispalindrome(str):
	str1 = str[::-1]
	if str1 == str:
		print("yes", str1, "is a palindrome")
	else:
		print("no")
	
ispalindrome("radar")

print("\n\n******WAP to palindrome with method-2***********")
def isPal(str):
 
    # Run loop from 0 to len/2 
    for i in range(0, int(len(str)/2)): #here we can take str/2 or just str as well 
        if str[i] != str[len(str)-i-1]: #need to understand this step
            return False
    return True
 
# main function
s = "malayalam"
ans = isPal(s)
 
if (ans):
    print("Yes")
else:
    print("No")

print("\n\n******WAP to palindrome with method-3***********")
def isP(s):
	rev=''.join(reversed(s))#for str to reverse we can use ''.join(reversed(s)) and for list
	if(s==rev):
		return True
	return False

s= "radar"
pal=s
if pal:
	print("Yes")
else: print("No")



my_list=
print("\n\nWAP to print last element as first by using split***********")
string= "I love India"
st=string.split() # this will split the string into elements and 
print(st[-1], st[0], st[1]) # here we are calling by using indexing
