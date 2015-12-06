from models.number import Number
from models.exceptions import *
from static.strings import STRINGS
from static.settings import *
from utils.random import *

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
                print("You chose to perform an addition.")

                base = self.readBase()
                leftTerm = self.readNumber(base)
                rightTerm = self.readNumber(base)

                if SETTINGS['showBase']:
                    print("%r + %r = %r" % (leftTerm, rightTerm, leftTerm + rightTerm))
                else:
                    print("%s + %s = %s" % (leftTerm.getValue(), rightTerm.getValue(), (leftTerm + rightTerm).getValue()))

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

    def readNumber(self, base):
        while True:
            value = input("Please enter a number (base %i): " % base)

            try:
                for i, symbol in enumerate(value):
                    if i == 0:
                        assert symbol == '-' or symbol in symbolsOfBase[base]
                    else:
                        assert symbol in symbolsOfBase[base]

                number = Number(value, base)
                break
            except AssertionError:
                print("Please enter a valid representation (e.g. %s)" % randomNumber(None, None, base).getValue())
            except Exception as e:
                print(e)
        return number

    def readBase(self):
        while True:
            base = input("The base of the addition: ")

            try:
                base = int(base)
                assert base in SETTINGS['bases']
                break
            except ValueError:
                print('The base must be an integer.')
            except AssertionError:
                print('The valid bases are: 2, 3, ..., 10, 16.')
            except Exception as e:
                print(e)
        return base
