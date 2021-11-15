def averager(*args):
     sum = 0
     for i in args:
            sum += i
     return sum/len(args)

#print(averager(1,2,3,4,5))

def newAverager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count


x = newAverager()
next(x)
x.send(10)
x.send(20)
print(x.send(30))