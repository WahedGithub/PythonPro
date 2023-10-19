s= input("enter the String:")
v_d={'A':0, 'E':0, 'I':0, 'O':0, 'U':0} #if we give lower case alphabets then it will not take the upper case ones from the string
for i in s:
	if i.upper() in v_d:
		v_d[i.upper()] +=1
print (v_d)