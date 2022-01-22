from contextlib import contextmanager

@contextmanager
def open_file(filename, mode):
    f = open(filename, mode)
    try:
        yield f
    finally:
        f.close()


def myFunction(func):
    def wrapper():
        print("before func is called")
        func()
        print("after func is called")
    return wrapper


@myFunction
def decFunc():
    with open_file("test.txt", "r") as f:
        print(f.read())


#decFunc = myFunction(decFunc)


decFunc()