def sum(arr):
	su=0
	for i in arr:
		su= su +i
	return su
#arr=[]
arr=[1,3,5,7]
#n= len(arr)
ans=sum(arr)
print("sum of array is", ans)
############################method -2################################
print("*****Another Method for finding the SUM*******")
arr=[12,3,4,15]
ans =sum(arr)
print(ans)

print("*****finding of maximum from array*****")
def largest(arr,n):
	max=arr[0]
	for i in range(1,n):
		if arr[i]> max:
			max= arr[i]
	return max
	
arr=[10,324,45,90]
n=len(arr)
ans=largest(arr,n)
print("Largest in given array is", ans)

print("\n\nanother simple method to find the maximum number")
arr=[1,2,3,4,6]
print(max(arr))
