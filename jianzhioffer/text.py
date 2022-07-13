from functools import wraps
import re
from typing import Any


def preserving_decorator(func):
    # print("test1")
    @wraps(func)
    def wrapper(*args, **kwargs):
        """The internal documentation of the wrapper function"""
        print(func.__name__)
        return func(*args, **kwargs)

    return wrapper


@preserving_decorator
def func_with_important_docstring():
    """This is the string we want to save"""
    print("啦啦啦")


# func_with_important_docstring()


def fibonacci(n):
    a, b = 0, 1
    while b < n:
        yield b
        a, b = b, a + b


# fib = fibonacci(5)

# try:
#     while True:
#         print(next(fib))
# except StopIteration:
#     pass


class RevealAccess(object):
    def __init__(self, interval=None, name="var"):
        self.val = interval
        self.name = name

    def __get__(self, obj, cls=None):
        print("Retrieving", self.name)

    def __set__(self, obj, value):
        print("Updating", self.name)
        self.val = value

    def __getattribute__(self, __name: str) -> Any:
        print("call __getattribute__")


class MyClass(object):
    x = RevealAccess(10, "var x")
    y = 5


# m = MyClass()


class Test:
    def __str__(self) -> str:
        return "1"

    def __repr__(self) -> str:
        return "2"


# t = Test()
import ipdb

ipdb.set_trace()

class Rectangel(object):

    @property
    def width(self) -> int:
        return self.width