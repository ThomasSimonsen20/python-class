import random

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

def students_list(num_students):
    result = []
    for i in range(num_students):
        person = {
            'id': i,
            'name' : random.choice(names),
            'major' : random.choice(majors)
        }
        result.append(person)
    return result

def students_generator(num_students):
    for i in range(num_students):
        person = {
            'id': i,
            'name' : random.choice(names),
            'major' : random.choice(majors)
        }
    yield person



people = students_list(1000000)
people = students_generator(1000000)