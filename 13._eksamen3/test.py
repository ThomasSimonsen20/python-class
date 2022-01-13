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
        print("Before we call our decorator function")
        func()
        print("After we call our decorator function")
    return wrapper

@my_decorator
def say_whee():
    with open_file('yeet.txt', 'r') as f:
        print(f.read())

say_whee()








##def say_whee():
    #print("Whee!")

#say_whee = my_decorator(say_whee)  

#x = say_whee()
#next(x) for at få hver af dem.


