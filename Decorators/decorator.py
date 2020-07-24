# decorator is a higher order function

def my_decorator(func):
    def wrap_func(*args,**kwargs):
        print('******')
        func(*args,**kwargs)
        print('******')
    return wrap_func

@my_decorator
def hello(greet):
    print('hellooooo '+ greet)
@my_decorator
def bye():
    print('see ya later')

hello('how are you')
# bye()
# hello2=my_decorator(hello)
# hello2()
#
# my_decorator(hello)()