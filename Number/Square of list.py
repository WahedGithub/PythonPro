l = [1,3,4,6,7]
for i in l: print (i**2, end=',') #this is working but printing the output in diff lines for each indexes

#[i**2 for i in l] # This is working in python idle but here its not giving any output

#for square of a number: num**2
## For square root of a number: num**(.5)

print("\n\n******WAP to find the sum square of given number******")
def squaresum(n):
	sum =0 # here we are taking sum as 0 coz 
	for i in range(1, n+1):
		sum = sum+ (i*i) #here we are keeping the sum as 0 only in all the iterations this is just to sumup the squared elements
	return sum# 1+4+9+16=30

n =4
print("square + sum of", n, "is", squaresum(4))

print("\n\n****Sum of square of first N natural numbers = (N*(n+1)*(2*(n+1))/6****")

#def sqsm(num):
#	return (num*(num+1)*(2*num+1)/6

#print(sqsm(5))## this is giving error need to look 


print("\n\n******WAP to find the cube sum of given number******")
def cubesum(n):
	sum =0 # here we are taking sum as 0 coz 
	for i in range(1, n+1):
		sum = sum+ (i*i*i) #here we are keeping the sum as 0 only in all the iterations this is just to sumup the squared elements
	return sum

n=5
print("Cube + sum of", n, "is", cubesum(5))