thisset = {"apple", "banana", "orange", "cherry", "pear"}
thisset.remove("banana") #or thisset.discard("banana")
print(thisset)
x = thisset.pop() #removes random item
print(x)
print(thisset)
thisset.clear()
print(thisset)
del thisset #if printing, will show an error
