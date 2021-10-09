import sys

#Create a commandline tool that checks if the required aguments are present when you run the program, 
#and if not tells you what is missing to run the program.
#If you run python python script.py the program should print an error saying Usage: 
# python script.py [-it]{--rm} where the [] means required and the {} means optional.

def main(argv):
    if len(argv) == 1:
        print('Usage: python 0._ex4.py [-it][--rm]')
    elif argv[1] != '-it':
        print('Usage: python 0._ex4.py [-it]{--rm}')
    elif len(argv) == 3 and argv[2] != '--rm':
        print('Usage: python 0._ex4.py [-it]{--rm}')
    elif len(argv) == 3 and argv[2] == '--rm':
        print('WTF IS HAPPENING')
    else:
        input()

    sys.exit

main(sys.argv)  

  

