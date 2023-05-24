from time import time

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


# hello()

def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'took {t2-t1} s')
        return result
    return wrapper


@performance
def long_time():
    for i in range(100000000):
        i*5


print(long_time())
