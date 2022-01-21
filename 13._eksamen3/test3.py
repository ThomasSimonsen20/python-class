from contextlib import contextmanager

@contextmanager
def open_file(filename, mode):
    f = open(filename, mode)
    try:
        yield f
    finally:
        f.close()

def my_decorator(func):
    def wrapper():
        print("Before func is called")
        func()
        print("After func is called")
    return wrapper

@my_decorator
def callDecorator():
    with open_file("yeet.txt", "r") as f:
        print(f.read())

#callDecorator = my_decorator(callDecorator)

callDecorator()