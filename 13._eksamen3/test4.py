from contextlib import contextmanager

@contextmanager
def open_file(filemode, r):
    f = open(filemode, r)
    try:
        yield f
    finally:
        f.close()
    


def myFunction(func):
    def wrapper():
        print("Before our func is called")
        func()
        print("After func is called")
    return wrapper

@myFunction
def func():
    with open_file("test.txt", "r") as f:
        print(f.read())

#func = myFunction(func())

func()