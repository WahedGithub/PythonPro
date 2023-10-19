def near_thousand(n):
	return((int(1000-n) <=100) or (int(2000-n)<=100))

print(near_thousand(1000))

def new_string(str):
	if len(str) >=2 and str[:2] =="Is":
		return str
	return "Is" + str

print(new_string("Array"))
print(new_string("IsEmpty"))

num = int(input("enter the number:"))
if num % 2 ==0: print("even")


str='123'
st1=list(str)
print(st1[0] + st1[1] + st1[2])