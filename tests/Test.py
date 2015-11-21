"""
    Module implements some tests.
"""

from random import randint
from models.Number import *

class Test:
    def __init__(self):
        pass

    def testAddition(self, testCount=100, valmax=10**18, verbose=False):
        """
            Method tests the "+" operator on Number objects in base 10.
        """
        for i in range(0, testCount):
            upperBound = valmax if randint(0, 1) == 0 else 10

            x = randint(0, upperBound)
            y = randint(0, upperBound)
            base = randint(2, 10)


            expected = str(x+y)
            actual = (Number(x, base) + Number(y, base)).getValue()

            if verbose:
                print("Addition test #%i" % (i+1))
                print("%i + %i" % (x, y))
                print("Expected result: %s\nActual result:   %s\n" % (expected, actual))

            assert expected == actual


    def testEverything(self, verbose=False):
        alright = True
        try:
            self.testAddition(verbose=verbose)
        except Exception as e:
            print("Addition test failed :(")
            print(e)
            alright = False

        if alright:
            print("All tests passed :)")

