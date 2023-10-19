print("form1 range(n)")
r= range(10)
print('\nThis will give the type of the vairaible:', type(r))
print("\nThis will print from 0 to the given number:", r)
for x in r:
	print(x)

#range(n) print from 0 to n-1----form 1
##range(begin, end) print from begin to end-1
print("\nform2 begin to end-1")
r1= range(1,10)
for x in r1:
 print(x)
 
print("\nform3 begin end increment")#range(begin, end, increment/decrement)
r3 = range(2,22,2)
for x in r3:
 print(x)
 
 
print("\nform4 begin end decrement")#range(begin, end, increment/decrement)
r4 = range(20,2,-2)
for x in r4:
 print(x)
 
print("\n indexing is applicable for range")
rr = range(10,21)
print(rr[0])
print(rr[-1])
print("\n slicing is applicable on range but rarely used")
#r1= rr[1:5]# Slicing is possible but used rarely in range
#for x in r1:
 #print(x)
print(rr[1:5])
print("\n range object is immutable")
#1. Sequence-when seq is required range comes into picture
#2. range(10), range(1,10), range(10,21,2)
#3. Order is imp, thats y index and slicing is applicable
#4. Its Immutable