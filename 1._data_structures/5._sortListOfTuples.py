a = [(1,2),(2,2),(3,2),(2,1),(2,2),(1,5),(10,4),(10, 1),(3, 1)]

def reverseIndex(tuples):
    return (tuples[1], tuples[0])

print(sorted(a, key=reverseIndex))