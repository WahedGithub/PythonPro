print("****Example 1: How range works in Python?****")
# empty range
print(list(range(0)))
list1 =[] ## another method to create empty list and print
print(list1)

# using range(stop)
print(list(range(10)))

# using range(start, stop)
print(list(range(1, 10)))

print("\n********Example 2: Create a list of even number between the given numbers using range()****")
start = 2
stop = 14
step = 2

print(list(range(start, stop, step)))

print("\n******8Example 3: How range() works with negative step?******")
start = 2
stop = -14
step = -2

print(list(range(start, stop, step)))

# value constraint not met: step value should be of same as stop
print(list(range(start, 14, step)))