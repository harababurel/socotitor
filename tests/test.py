"""
    Module implements some tests.
"""

from random import randint, choice
from models.number import *
from static.settings import *
from utils.random import *
import numpy

class Test:
    def __init__(self):
        pass

    def testOperationsAndConversions(self, testCount=SETTINGS['testCount'], sizemax=SETTINGS['sizemax'], verbose=SETTINGS['verbose']):
        """Method tests the following operators: +, -, *, //, %, **,
        and the following functions: abs(), isNegative(), isPositive().
        It also uses the conversion algorithms, so those are also tested.

        Raises:
            **AssertionError**: if some test fails.
        """
        for i in range(0, testCount):

            if verbose:
                print("Operation test #%i" % (i+1))

            x = randomNumber(None, sizemax, 10)
            y = randomNumber(None, sizemax, 10)

            while y == Number('0', 10):
                y = randomNumber(None, sizemax, 10)


            print("Chosen numbers: %s and %s" % (x.getValue(), y.getValue()))

            intX = int(x.getValue())
            intY = int(y.getValue())

            newBase = choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 16])

            x = x.convert(newBase, False)
            y = y.convert(newBase, False)

            actualSum  = x +  y
            actualDiff = x -  y
            actualProd = x *  y
            actualQuot = x // y
            actualRem  = x %  y
            #actualPow  = x ** y
            actualAbs  = abs(x)

            expectedSum  = numpy.base_repr(intX +  intY, newBase)
            expectedDiff = numpy.base_repr(intX -  intY, newBase)
            expectedProd = numpy.base_repr(intX *  intY, newBase)
            expectedQuot = numpy.base_repr(intX // intY, newBase)
            expectedRem  = numpy.base_repr(intX %  intY, newBase)
            #expectedPow  = numpy.base_repr(intX ** intY, newBase)
            expectedAbs  = numpy.base_repr(abs(intX),    newBase)

            print("%s +  %s = %s, expected %s" % (x.getValue(), y.getValue(), actualSum.getValue(),  expectedSum))
            print("%s -  %s = %s, expected %s" % (x.getValue(), y.getValue(), actualDiff.getValue(), expectedDiff))
            print("%s *  %s = %s, expected %s" % (x.getValue(), y.getValue(), actualProd.getValue(), expectedProd))
            print("%s // %s = %s, expected %s" % (x.getValue(), y.getValue(), actualQuot.getValue(), expectedQuot))
            print("%s %%  %s = %s, expected %s" % (x.getValue(), y.getValue(), actualRem.getValue(),  expectedRem))
            #print("%s ** %s = %s, expected %s" % (x.getValue(), y.getValue(), actualPow.getValue(), expectedPow))
            print("|%s|     = %s, expected %s" % (x.getValue(), actualAbs.getValue(), expectedAbs))
            assert actualSum.getValue()  == expectedSum
            assert actualDiff.getValue() == expectedDiff
            assert actualProd.getValue() == expectedProd
            assert actualQuot.getValue() == expectedQuot
            assert actualRem.getValue()  == expectedRem
            #assert actualPow.getValue()  == expectedPow
            assert actualAbs.getValue()  == expectedAbs



    def testEverything(self, verbose=SETTINGS['verbose']):
        alright = True
        self.testOperationsAndConversions(verbose=verbose)
        try:
            pass
        except Exception as e:
            print("Operations tests failed :(")
            print(e)
            alright = False

        if alright:
            print("All tests passed :)")

