import datetime

""" 
1. Model an organisation of employees, management and board of directors in 3 sets.

Board of directors: Benny, Hans, Tine, Mille, Torben, Troels, Søren

Management: Tine, Trunte, Rane

Employees: Niels, Anna, Tine, Ole, Trunte, Bent, Rane, Allan, Stine, Claus, James, Lars

    who in the board of directors is not an employee?
    who in the board of directors is also an employee?
    how many of the management is also member of the board?
    All members of the managent also an employee
    All members of the management also in the board?
    Who is an employee, member of the management, and a member of the board?
    Who of the employee is neither a memeber or the board or management? 
"""

directors = {'Benny', 'Hans', 'Tine', 'Mille', 'Torben', 'Troels', 'Søren'}
management = {'Tine', 'Trunte', 'Rane'}
employees = {'Niels', 'Anna', 'Tine', 'Ole', 'Trunte', 'Bent', 'Rane', 'Allan', 'Stine', 'Claus', 'James', 'Lars'}

print(directors - employees)
print(employees.intersection(directors))
print(len(directors.intersection(management)))
print(management.intersection(employees))
print(management.intersection(directors))
print(management.intersection(directors).intersection(employees))
print(employees.difference(management).difference(directors))


######################################################################################
""" 
2.Using a list comprehension create a list of tuples from the folowing datastructure

{‘a’: ‘Alpha’, ‘b’ : ‘Beta’, ‘g’: ‘Gamma’}
"""

a = {'a': 'Alpha', 'b' : 'Beta', 'g': 'Gamma'}

listOfTuples = [x for x in a]

print(a)

######################################################################################

""" 
3. From these 2 sets:

{'a', 'e', 'i', 'o', 'u', 'y'}
{'a', 'e', 'i', 'o', 'u', 'y', 'æ' ,'ø', 'å'} 
"""

a = {'a', 'e', 'i', 'o', 'u', 'y'}
b = {'a', 'e', 'i', 'o', 'u', 'y', 'æ' ,'ø', 'å'}

print(a.union(b))
print(a.symmetric_difference(b))
print(a.difference(b)) #a indeholder samme som b, derfor retunere set()?
print(a.intersection(b))

######################################################################################

""" 
4. Date Decoder.

A date of the form 8-MAR-85 includes the name of the month, which must be translated to a number.

Create a dict suitable for decoding month names to numbers.

Create a function which uses string operations to split the date into 3 items using the "-" character.

Translate the month, correct the year to include all of the digits.

The function will accept a date in the "dd-MMM-yy" format and respond with a tuple of ( y , m , d ). 
"""

def convertDate(date):
    newDate = date.split("-")
    month_number = datetime.datetime.strptime(newDate[1], '%b').month
    return (newDate[2], month_number, newDate[0])


print(convertDate('2-jan-91'))