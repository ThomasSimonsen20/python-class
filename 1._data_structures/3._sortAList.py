
a = ['Claus', 'Ib', 'Per', 'Adam', 'Peter', 'Maya', 'Olivia']

print(sorted(a))
print(sorted(a, reverse=True))
print(sorted(a, key=len))
print(sorted(a, key = lambda x:x[-1]))