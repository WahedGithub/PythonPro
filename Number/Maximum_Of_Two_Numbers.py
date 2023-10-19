def maxi(a,b):
	if a>=b:
		print(a, "is maximum than", b)
		#return a
	else:
		print (b, "is maximum than", a)
		#return b
		
maxi(3,2)

print ("\n*******Another Method to find the Maximum number using max() function********")
a, b = 2, 5
maximum = max(a,b)
print(maximum)


l = [1,4,9]
print(max(l))
