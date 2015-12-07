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

            elif command in ['+', '-', '*', '/', '^']:
                print("You chose to perform %s." % STRINGS['operationNamesWithPrefix'][command])

                base = self.readBase(command)
                leftTerm = self.readNumber(base)
                rightTerm = self.readNumber(base)

                try:
                    if command == '+':
                        result = leftTerm + rightTerm
                    elif command == '-':
                        result = leftTerm - rightTerm
                    elif command == '*':
                        result = leftTerm * rightTerm
                    elif command == '/':
                        result = (leftTerm // rightTerm, leftTerm % rightTerm)
                    elif command == '^':
                        result = leftTerm ** rightTerm

                except Exception as e:
                    print(e)
                    continue

                if SETTINGS['showBase']:
                    print("%r %s %r = " % (leftTerm, command, rightTerm), end='')

                    if command == '/':      # need to print two results in this case
                        print("%r, remainder %r" % result)
                    else:
                        print("%r" % result)
                else:
                    print("%s %s %s = " % (leftTerm.getValue(), command, rightTerm.getValue()), end='')

                    if command == '/':      # need to print two results in this case
                        print("%s, remainder %s" % (result[0].getValue(), result[1].getValue()))
                    else:
                        print("%s" % result.getValue())

            elif command == 'c':
                print("You chose to perform %s." % STRINGS['operationNamesWithPrefix'][command])

                oldBase = self.readBase(command, "Please enter the initial base: ")
                number = self.readNumber(oldBase)
                newBase = self.readBase(command, "Please enter the new base: ")

                result = number.convert(newBase)

                print("%r = %r" % (number, result))

            elif command == 'h':
                print(STRINGS['help'])

            elif command == 'x':
                exit(0)

            else:
                print("Command not recognized. Try 'h' for help.")

    def readNumber(self, base, message=None):
        while True:
            if message is None:
                value = input("Please enter a number (base %i): " % base).upper()
            else:
                value = input(message)

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

    def readBase(self, operation, message=None):
        while True:
            if message is None:
                base = input("The base of the %s: " % STRINGS['operationNamesWithoutPrefix'][operation])
            else:
                base = input(message)

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
