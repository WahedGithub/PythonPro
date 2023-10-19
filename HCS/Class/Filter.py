##This is working in shell

x1 = list(range(3,30))
f = lambda x:x% 3 == 0
f(10)
f(9)
list(filter(f, x1))

