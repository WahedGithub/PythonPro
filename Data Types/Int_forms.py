print("Note: in which ever format it is python will print the values in decimal format(base 10)")

print("first one is decimal format with base 10 ex: a =10/20\n")

print("Binary Form Under Data Types")#only 0 & 1 can be taken here
a = 0B1111 ##0B/b is the code for defining binary number so here it will be 2^3,2^2,2^1,2^0, Base 2
print('0B1111=' ,a)##8+4+2+1 here 2^0 is zero but that one after binary comes down so it becomes 15

print("Octal Form Under Data Types")# numbers from 0-7 can b taken
a=0o123 #0o/O is the code, and base is 8, so 8^2,8^1,8^0 & 1*64+2(8)+3(1 as 8^0=1)=83
print('0o123=', a)

##a= 0o786##it will throw an error as 8 is der###################################################

print("Hexa Decimal Form Under Data Types")# numbers from 0-9 & A-F/a-f(10-15) can b taken with base 16
a= 0x10## 0x/X is the code, and base is 16, so 16^1, 16^0
print('0x10=', a)

print("Hexa Decimal with name")
a= 0XFace##it will take as it is between a-f 15(16)^3+10(16)^2+13(16)^1+14(16)^0
print('0XFace=' ,a)

print("Hexa Decimal Others names are")
a= 0XBeef
print('0xBeef=' ,a)

#a= 0XBeer this will through error as 'r' available in it.
#print(a)