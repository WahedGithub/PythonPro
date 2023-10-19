##WAP to get an 6 digit OTP

from random import randint
print(randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9))##this is with space

print("\nSep") ##Sep='' without space is to remove space
from random import randint
print(randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),sep='') ## without space


print("\nRange")
from random import randint
for i in range(3): # to print multiple OTP apply range
	print(randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),sep='')