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

            elif command == 'x':
                exit(0)

            else:
                print("Command not recognized. Try 'h' for help.")

