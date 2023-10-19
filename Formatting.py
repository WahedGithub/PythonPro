name = 'john'
age = 25
sal = 10000.25

print('\nApproach--1 Printing in single line')
print(name,age,sal)

print('\nApproach--2 printing in different lines')
print("Name is: ", name)
print("Age is: ", age)
print("Salary is: ", sal)

print('\nApproach--3 using % operator Here type is important')
print("if we take %f then it will print four zeros extra thats y %g is taken")
print("Name: %s Age:%d Salary:%g" %(name, age , sal)) # %f or %g can be used for decimal/float

print('\nApproach--4 using .format{} --Here value is imp')
print("Name:{} Age:{} Salary:{}". format(name,age,sal))

print('\nApproach--5 using .format{} here values are required type is not important here')
print("Name:{} Age:{} Salary:{}". format(age,age,age))

print('\nApproach--6 using index + .format{}')
print("Name:{0} Age:{1} Salary:{2}". format(name,age,sal)) #so here it will take index[0]=name

print('\nApproach--7 using same index + .format{}')
print("Name:{0} Age:{0} Salary:{0}". format(name,age,sal)) # printing same index