
li = []
for i in range(1, 10):
    li.append(i)
#print(li)

listComp = [i for i in range(1, 10)]
#//list comprehensions, 3 mindre linjer. Nemmere at bruge end ovenover.
#print(listComp)


#Create a list of capital letters in the english alphabet
aplhaComp = [chr(i) for i in range(65,91)]
#print(aplhaComp)

alphabet = []
for i in range(65,91):
    alphabet.append(chr(i))
#//Hvis man skulle lave på den anden måde

#Create a list of capital letter from the english aplhabet, but exclude 4 with the Unicode code point of either 70, 75, 80, 85.
aplhaCompWithOut = [chr(i) for i in range(65,91) if i not in [70, 75, 80, 85]]
#print(aplhaCompWithOut)

#Create a list of capital letter from from the english aplhabet, but exclude every second between F & O
aplhaCompFAndO = [chr(i) for i in range(65,91) if i not in range(70,80, 2)]
#print(aplhaCompFAndO)

[i for i in range(1, 10, 2)]
#//ulige tal 1,3,5 osv
[i for i in range(1, 10) if i%2 == 0]
#//lige tal 2,4,6 osv
[i if i%2 == 0 else 'Non-even' for i in range(1,10)]
#//hvis man bruger else skal ens if else være foran resten.

#########
li = []
for i in range(3):
    for j in range(2):
        li.append((i,j))
#print(li)
[(i,j) for i in range(3) for j in range(2)]
#########

#From 2 lists, using a list comprehension, create a list containing:
colors = ['Black', 'White']
sizes = ['s', 'm', 'l', 'xl']
#print([(c,s) for c in colors for s in sizes])
#//(c,s) er de variable navner som vi sætter info in på, ud fra colors og sizes

#If the tuple pair is in the following list, it should not be added to the comprehension generated list.
soled_out = [('Black', 'm'), ('White', 's')]
#print([(c,s) for c in colors for s in sizes if (c,s) not in soled_out])
