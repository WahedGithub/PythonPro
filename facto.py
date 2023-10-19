#s=input("Enter the string:   ")
#s = s[:12:1]
#print (s)

def fact(n):
	return 1 if (n==0 or n ==1) else n* fact(n-1);

#print(fact(3))

n =5
print("factorial of", n, "is", fact(n))

print("\nanother mehtod")
# Python 3 program to find 
# factorial of given number 
def factorial(num): 
	if num < 0: 
		return 0
	elif num == 0 or num == 1: 
		return 1
	else: 
		fact = 1
		while(num > 1): 
			fact *= num 
			num -= 1
		return fact 

# Driver Code 
num = 4; 
print("Factorial of",num,"is", 
factorial(num)) 

# This code is contributed by Dharmik Thakkar 
