from functools import reduce
# map

def multiply_by2(li):
    # for item in li:
    #     new.append(item*2)
    return li*2
# map loops through all the items in the iterable
print(list(map(multiply_by2,[1,2,3])))

# Filter
def check_odd(item):
    return item % 2
print(list(filter(check_odd,[1,3,5,4])))

# zip
print(list(zip([1,2,3],[4,5,6],[7,8,9])))

# Reduce
def accumulator(acc, item):
    print(acc,item)
    return acc+item

print(reduce(accumulator,[1,2,3],0))