print("WAP to create a new list L2 from L1 without duplicates") 
l1 = [1,1,2,2,3,3,4,5,6,6,5,8]
l2 =[] # assign the list or string value to different variable and then use the loops
for i in l1:
	if i not in l2:
		l2.append(i)
		#print ("removing ",i)
print (l2)