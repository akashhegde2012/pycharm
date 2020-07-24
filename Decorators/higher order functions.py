# @classmethod
# @staticmethod

# def hello():
#     print('hellooooo')
# greet=hello()
# print(greet)

def hello(func): # higher order function if it accepts another function as a parameter
    func()
def greet():
    print('still here')
a=hello(greet)
print(a)