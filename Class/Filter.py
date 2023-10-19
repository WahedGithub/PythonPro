##This is working in shell

x1 = list(range(3,30))
f = lambda x:x% 3 == 0
print(f(10))## here we are defining x =10
print(f(9))
print(list(filter(f, x1)))

