# lambda expression
# lambda param: action(param)

print(list(map(lambda item: item*2,[1,2,3,4,5])))
g=lambda x:x+22
print(g(4))
print(list(filter(lambda x:x%2,[1,2,3,4,5])))

# lambda espression to square our list
print(list(map(lambda x : x**2,[1,2,3,5,6])))

# List sorting
a=[(0,2),(4,3),(9,9),(10,-1)]
a.sort(key=lambda x: x[1])
print(a)