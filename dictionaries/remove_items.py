thisdict = {
    "brand": "BMW",
    "model": "m5",
    "year": 2023,
    "color": "black"
}
thisdict.pop("model")
print(thisdict)
thisdict.popitem() #pops the last item
print(thisdict)
del thisdict["brand"]
print(thisdict)
thisdict.clear()
print(thisdict)