

def generator_func(num):
    for i in range(num):
        yield i

g=generator_func(100)
next(g)
next(g)
print(next(g))
# for item in generator_func(1000):
#     print(item)

