list1 = ["m", "l", "a"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
for x in list2:
    list1.append(x)
print(list1)
list2.extend(list1)
print(list2) 