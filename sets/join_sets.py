# union
thisset = {"apple", "banana", "cherry", "pear", "orange"}
set2 = {1, 2, 3, 4}
set3 = thisset.union(set2) #or set3 = thisset | set2, but not with other data types
print(set3)

#intersection
set1 = {"apple", "banana", "orange"}
set2 = {"google", "microsoft", "apple", "banana"}
set3 = set1.intersection(set2) # or use & sign
print(set3)
set1.intersection_update(set2)
print(set1)

#difference
myset = {"apple", "mazda", "picture"}
myset2 = {"circle", "rectangle", "apple"}
set4 = myset.difference(myset2) # or use - sign
print(set4)

#symmetric difference
set1 = {"square", "triangular", "rectangular"}
set2 = {"apple", 'circle', "square"}
set3 = set1.symmetric_difference(set2) # or use ^ sign
print(set3)