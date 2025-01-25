thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for x in thisdict:
    print(x) #prints all key names, or for x in thisdict.keys():
for x in thisdict:
    print(thisdict[x]) #prints all values, or for x in thisdict.values():
for x, y in thisdict.items():
    print(x,y) #prints all keys and values