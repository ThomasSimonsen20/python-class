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
        print("Before our function is called")
        func()
        print("After our function is called")
    return wrapper


@my_decorator
def call_decorator():
    with open_file("test.txt", "r") as f:
        print(f.read())

#call_decorator = my_decorator(call_decorator)

call_decorator()