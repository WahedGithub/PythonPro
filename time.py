import time

tick = time.time()
localtime = time.localtime(time.time()) #Example 1
print (localtime)


print("""Another format of time
is as below""")
#below format will be as normal one
localtime = time.asctime( time.localtime(time.time()) ) #Example 2----if asctime is added then it will give the output in simple format

print(localtime)