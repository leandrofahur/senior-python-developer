# higher order functions
def greet(func):
    func()


def greet2():
    def func():
        return 5
    return func

# Decorator is a function that takes another function as an argument,
# adds some kind of functionality and then returns another function,
# all of this without altering the source code of the original function that we passed in.


def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('********')
        func(*args, **kwargs)
        print('********')
    return wrap_func


# @my_decorator
# def hello(greeting):
#     print(greeting)


# hello('hi')

@my_decorator
def hello(greeting='hi', emoji=':('):
    print(greeting, emoji)


hello()
