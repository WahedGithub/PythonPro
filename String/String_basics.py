print("String basics")
a= '''triple quotes are 
		used to define multiple 
		line string literall'''
## triple quotes properties 
##1. Triple quotes are used to define multiple line string literall
##2. To use ' and " as normal characters in our string '''/""" quotes are used
##3. To define doc string
		
print(a)

print('it can be single' ',' 'triple quotes or double triple quotes')

s= "class by 'durga' on youtube is very good"## if want to get any word in quotes inside string use quotes like this

print(s)

d = 'class by "durga" on youtube is very good' ##

print('this is opp of s varaible:',d)

t = '''class by 'durga' on "youtube" is very good''' 

print(t)


def count_Char(str):
	upper =0
	for i in str:
		if str[i] >= 'A' and str[i] <='Z' : upper +=1
	return upper

str= "Australia won the world cup 2015 on 29th Mar"
u =count_Char(str)
print (u)
