l = ['a', 'b', 'c']

try:
    print("1. Inside try")
    print("2. About to do something bad")
    l[3]
    print("3. After doing something bad")
except:
    print("4. Caught the exception")
print("5. And exiting")