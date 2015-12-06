from models.number import Number
from models.exceptions import *
from static.strings import STRINGS

class Console():
    def __init__(self):
        pass

    def run(self):
        print(STRINGS['title'])
        print(STRINGS['help'])

        while True:

            command = input('> ')

            if command == '':
                continue

            elif command == '+':
                print("+ not implemented yet")

            elif command == '-':
                print("- not implemented yet")

            elif command == '*':
                print("* not implemented yet")

            elif command == '/':
                print("/ not implemented yet")

            elif command == 'c':
                print("c not implemented yet")

            elif command == 'h':
                print(STRINGS['help'])

            elif command == 'x':
                exit(0)

            else:
                print("Command not recognized. Try 'h' for help.")

