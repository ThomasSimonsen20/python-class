
from types import resolve_bases


def fibonacci():
    sum = 1
    lastSum = 1
    totalSum = 0
    evenSum = 0
    while totalSum < 4000:
        z = (sum + lastSum)
        if z%2 == 0:
            evenSum = evenSum + z
        

        sum = lastSum
        lastSum = totalSum

    print(evenSum)

fibonacci()