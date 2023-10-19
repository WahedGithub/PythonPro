x=7
def f():
	global x# have ot define global x if this need to be considered
	y=x
	print(y)
	x=2
	
f()
