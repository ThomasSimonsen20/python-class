
#Create a commandline tool that checks if the required aguments are present when you run the program, 
#and if not tells you what is missing to run the program.
#If you run python python script.py the program should print an error saying Usage: 
# python script.py [-it]{--rm} where the [] means required and the {} means optional.

import sys

def main(argv):
<<<<<<< HEAD
    if argv[1] != '-it':
        print('Usage: python script.py [-it]{--rm}')
    if len(argv) == 3 and argv[2] != '--rm':
        print('Usage: python script.py [-it]{--rm}')
=======
    if len(argv) == 1:
        print('Usage: python 0._ex4.py [-it][--rm]')
    elif argv[1] != '-it':
        print('Usage: python 0._ex4.py [-it]{--rm}')
    elif len(argv) == 3 and argv[2] != '--rm':
        print('Usage: python 0._ex4.py [-it]{--rm}')
>>>>>>> 521218fe405c6e7b10cb6135f985c01bdda7d969
    elif len(argv) == 3 and argv[2] == '--rm':
        print('Goodby')
    else:
        input()

<<<<<<< HEAD
    sys.exit()
=======
    sys.exit

main(sys.argv)  

  
>>>>>>> 521218fe405c6e7b10cb6135f985c01bdda7d969

main(sys.argv)
