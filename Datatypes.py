list=[1,2,3]
list.append(2)
print('new list:', list)
list.extend([12,3,4,5])
print("list with extend:", list)
list.insert(2,4)
print(list)

l=[]
for i in range(1,4):
    l.append(i)
print('append list=', l)

print('\ncopy list')
print(l.copy())


