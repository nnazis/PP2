def myfunc(n):
    return abs(n - 50)
thislist = [50, 200, 100,  39, 84]
thislist.sort(key = myfunc)
print(thislist)
mylist = ["banana", "Orange","Mango", "cherry"]
mylist.sort()
print(mylist)
mylist.sort(key = str.lower)
print(mylist)
mylist.reverse()
print(mylist)
