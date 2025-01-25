x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "mango"
y.append("orange")
x = tuple(y)
print(x)
#adding tuple to tuple
m = ("orange",)
x += m
print(x)