"""
    Module implements some tests.
"""

from random import randint, choice
from models.number import *
from static.settings import *

class Test:
    def __init__(self):
        pass

    def testAddition(self, testCount=SETTINGS['testCount'], valmax=SETTINGS['valmax'], verbose=SETTINGS['verbose']):
        """
            Method tests the "+" operator on Number objects in base 10.
        """
        for i in range(0, testCount):
            upperBound = valmax if randint(0, 1) == 0 else 10

            x = randint(0, upperBound)
            y = randint(0, upperBound)
            base = choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 16])

            base = 10 #override


            expected = str(x+y)
            actual = (Number(str(x), base) + Number(str(y), base)).getValue()

            if verbose:
                print("Addition test #%i" % (i+1))
                print("%i + %i" % (x, y))
                print("Expected result: %s\nActual result:   %s\n" % (expected, actual))

            assert expected == actual


    def testEverything(self, verbose=SETTINGS['verbose']):
        alright = True
        try:
            self.testAddition(verbose=verbose)
        except Exception as e:
            print("Addition test failed :(")
            print(e)
            alright = False

        if alright:
            print("All tests passed :)")

