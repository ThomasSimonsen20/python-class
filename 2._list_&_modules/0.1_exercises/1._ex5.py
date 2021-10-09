# os_exercise.py
# Do the following task using the os module

#1. create a folder and name the folder 'os_exercises.'                                                  
#2. In that folder create a file. Name the file 'exercise.py'                                                                            
#3. get input from the console and write it to the file.                                                 
#4. repeat step 2 and 3 (name the file something else).                                                  
#5. read the content of the files and and print it to the console.

import os

#1
os.mkdir('os_exercises')

#2
os.chdir('os_exercises')
open('exercise.py', 'w')

#3
typedInfo = input('Write something')
with open ('exercise.py', 'w') as f:
    f.write(typedInfo)

#4
typedInfo = input('Write something new')
with open ('exercise2.py', 'w') as f:
    f.write(typedInfo)

with open('exercise.py', 'r') as f1:
    with open('exercise2.py', 'r' ) as f2:
        print(f1.read() + f2.read())


#With open bruger man til at åbne filer, 'r' og 'w' er read / write.
#f er bare et variable navn, kunne være file or w/e
#input giver prompt til at skrive noget.