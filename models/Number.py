"""
    Module implements the Number class.
"""
from models.Exceptions import *

class Number:
    """
        The Number class models an integer value in some base.
    """

    def __init__(self, value=0, base=10):
        """
            If not provided, the base is considered to be 10,
            and the value is considered to be 0.
        """
        self.__base = base
        self.__digits = [x for x in str(value)[::-1]]
        self.__size = len(self.__digits)

    def __repr__(self):
        return "%s(%s)" % (self.getValue(), self.__base)

    def getBase(self):
        return self.__base

    def getValue(self):
        return ''.join(self.getDigits()[::-1])

    def getDigits(self):
        return self.__digits

    def getDigitAtPos(self, i):
        if 0 <= i and i < self.getSize():
            return int(self.__digits[i])
        return 0

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

        resultValue = int(''.join([str(digit) for digit in resultDigits[::-1]]))
        return Number(resultValue, self.getBase())


