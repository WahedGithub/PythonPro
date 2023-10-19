print("\n****WAP with break=breaks the statement when its meets statement*******")

for i in range(1,11):
	if i ==7:
		break
	else:
		print(i, end=" ")
		

print("\n****WAP with continue= continues without printing the found element statement*******")		
for i in range(1,11):
	if i ==7:
		continue
	else:
		print(i, end=",")
		
print("\n****WAP with pass=it just passes the statement*******")
for i in range(1,11):
	if i ==7:
		pass
	else:
		print(i, end=" ")