"""
    Module implements the Number class.
"""
from models.exceptions import *
from static.settings import *

class Number:
    """
        The Number class models an integer value in some base.
        Attributes:
            self.__base:   positive int -> the base of the number
            self.__sign:   0 or 1       -> the sign of the number (0 for positive, 1 for negative)
            self.__digits: list of ints -> the digits of the number, in reverse order
            self.__size:   int          -> the number of digits
    """

    def __init__(self, value='0', base=10):
        """
            If not provided, the base is considered to be 10,
            and the value is considered to be '0'.

            Arguments:
                value: string       (optional)
                base:  positive int (optional)
        """
        if base < 1:
            raise BaseError("The base %i is not defined." % base)

        self.__base = base

        if value[0] == '-':     # if the minus sign is provided
            self.__sign = 1     # then the number is negative
            value = value[1:]   # and the sign can be erased

        elif value[0] == '+':   # if the plus sign is provided
            self.__sign = 0     # then the number is positive
            value = value[1:]   # and the sign can be erased

        else:                   # if no sign is provided
            self.__sign = 0     # then the number is positive

        self.__digits = [symbolToDigit[x] for x in value[::-1]]
        self.__size = len(self.__digits)

        if int(max(self.__digits)) >= base:
            raise DigitError()

    def __repr__(self):
        """
            The format for representing a number in some base is:
            <value> + '_' + <base>

            Examples: 5_10, -1010110_2, 123_4
        """
        return "%s_%s" % (self.getValue(), self.__base)

    def getBase(self):
        return self.__base

    def getValue(self):
        return ['', '-'][self.isNegative()] + ''.join([digitToSymbol[x] for x in self.getDigits()][::-1])

    def getDigits(self):
        return self.__digits

    def getDigitAtPos(self, i):
        if 0 <= i and i < self.getSize():
            return int(self.getDigits()[i])
        return 0

    def isPositive(self):
        return self.__sign == 0

    def isNegative(self):
        return self.__sign == 1

    def getSize(self):
        return self.__size

    def __add__(self, other):
        """
            Method returns the result of self + other.
        """

        if self.getBase() != other.getBase():
            raise BaseError()

        resultDigits = []
        carry = 0
        for i in range(0, max(self.getSize(), other.getSize())):
            currentDigit = self.getDigitAtPos(i) + other.getDigitAtPos(i) + carry

            carry = currentDigit // self.getBase()
            currentDigit %= self.getBase()

            resultDigits.append(currentDigit)

        if carry > 0:
            resultDigits.append(carry)

        resultValue = int(''.join([digitToSymbol[digit] for digit in resultDigits[::-1]]))
        return Number(resultValue, self.getBase())


