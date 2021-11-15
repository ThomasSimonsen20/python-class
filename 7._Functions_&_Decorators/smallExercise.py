"Write a decorator that writes to a log file the time stamp of each time this function is called."
"Change the log decorator to also printing the values of the argument together with the timestamp."
"Print the result of the decorated function to the log file also."
"Create a new function and call it printer(text) that takes a text as parameter and returns the text. Decorate it with your logfunction. Does it work?"

import datetime

def log(func):
    def wrapper(*args):
        f = open('log.txt', 'a+')
        f.write(f'{datetime.datetime.now()}, {args}, {func(*args)}\n')
        return func(*args)
    return wrapper

@log
def add(*args):
    sum = 0
    for i in args:
        sum += i 
    return sum

@log
def printer(text):
    print('From printer')