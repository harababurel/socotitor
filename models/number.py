"""
    Module implements the Number class.
"""
from models.exceptions import *
from static.settings import *
from copy import deepcopy

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

        if not isinstance(value, str):
            raise TypeError("The value must be a <class 'str'>, not %r." % type(value))

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

        if len(self.__digits) > 0 and max(self.__digits) >= base:
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

    def getSign(self):
        return self.__sign

    def setSign(self, sign):
        self.__sign = sign

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

    def __neg__(self):
        """
            Method implements behaviour for negation (e.g. -someObject)
        """

        negative = deepcopy(self)

        if negative.getDigits() == [0]:
            return negative

        negative.setSign([1, 0][negative.getSign()])
        return negative

    def __abs__(self):
        """
            Method implements behaviour for absolute value (e.g |someObject|)
        """

        if self.isNegative():
            return -self
        return self

    def compare(self, a, b):
        """
            Method compares two numbers in the same base.
            TODO: make it work for different bases.

            Method returns:
                negative, if a < b
                0,        if a = b
                positive, if a > b
        """

        if a.getBase() != a.getBase():
            raise BaseError()

        # different signs
        if a.isNegative() and b.isPositive():
            return -1
        if a.isPositive() and b.isNegative():
            return 1

        # same signs, different sizes
        if a.getSize() < b.getSize():
            return -1 if a.isPositive() else 1
        if a.getSize() > b.getSize():
            return 1 if a.isPositive() else 1

        # same signs, same sizes, different digits
        for x in zip(a.getDigits()[::-1], b.getDigits()[::-1]):   # fixed bug: digits should be taken in reverse order
            if x[0] == x[1]:
                continue
            return -1 if x[0] < x[1] else 1

        # same signs, same sizes, same digits (-> equal)
        return 0

    def __lt__(self, other):
        return self.compare(self, other) < 0

    def __le__(self, other):
        return self.compare(self, other) <= 0

    def __eq__(self, other):
        return self.compare(self, other) == 0

    def __ne__(self, other):
        return self.compare(self, other) != 0

    def __ge__(self, other):
        return self.compare(self, other) >= 0

    def __gt__(self, other):
        return self.compare(self, other) > 0

    def positiveAddition(self, a, b):
        """
            Method returns the result of a + b.
            Note: <a> and <b> must both be positive.
            An exception is raised if this does not hold.
        """
        if a.isNegative() or b.isNegative():
            raise SignError()

        resultDigits = []
        carry = 0
        for i in range(0, max(a.getSize(), b.getSize())):
            currentDigit = a.getDigitAtPos(i) + b.getDigitAtPos(i) + carry

            carry = currentDigit // a.getBase()
            currentDigit %= a.getBase()

            resultDigits.append(currentDigit)

        if carry > 0:
            resultDigits.append(carry)

        resultValue = ''.join([digitToSymbol[digit] for digit in resultDigits[::-1]])
        return Number(resultValue, a.getBase())

    def positiveSubtraction(self, a, b):
        """
            Method returns the result of a - b.
            Note: <a> must be greater than (or equal to) <b>.
            <a> and <b> must have the same base.
            An exception is raised if this does not hold.
        """

        """
        void Subtract(Huge A, Huge B)
        /* A <- A-B */
        { int i, T=0;
         
          for (i=B[0]+1;i<=A[0];) B[i++]=0;
          for (i=1;i<=A[0];i++)
            A[i]+= (T=(A[i]-=B[i]+T)<0) ? 10 : 0;

            /* Adica A[i]=A[i]-(B[i]+T);
               if (A[i]<0) T=1; else T=0;
               if (T) A[i]+=10; */

          while (!A[A[0]]) A[0]--;
        }
        """

        if a.getBase() != b.getBase():
            raise BaseError()

        if a.isNegative() or b.isNegative():
            raise SignError()

        if a < b:
            raise ComparisonError()

        carry = 0
        resultDigits = []
        for i in range(0, a.getSize()):

            currentDigit = a.getDigitAtPos(i) - carry
            if i < b.getSize():
                currentDigit -= b.getDigitAtPos(i)

            carry = 1 if currentDigit < 0 else 0
            if carry:
                currentDigit += a.getBase()

            resultDigits.append(currentDigit)

        while len(resultDigits) > 1 and resultDigits[-1] == 0:
            resultDigits.pop()

        resultValue = ''.join([digitToSymbol[digit] for digit in resultDigits[::-1]])
        return Number(resultValue, a.getBase())

    def __add__(self, other):
        """
            Method returns the result of self + other.
            If self and other have the same sign, then sameSignAddition() is applied.
            Otherwise, sameSignSubtraction() is applied.
        """

        if self.getBase() != other.getBase():
            raise BaseError()

        if self.getSign() == other.getSign():
            if self.isPositive():
                return self.positiveAddition(self, other)
            else:
                return -self.positiveAddition(abs(self), abs(other))
        else:
            if abs(self) >= abs(other):

                if self.isPositive():
                    # greater positive + smaller negative = positive result
                    return self.positiveSubtraction(abs(self), abs(other))
                if self.isNegative():
                    return -self.positiveSubtraction(abs(self), abs(other))
            else:
                # smaller positive + greater negative = negative result

                if self.isNegative():
                    return self.positiveSubtraction(abs(other), abs(self))
                if self.isPositive():
                    return -self.positiveSubtraction(abs(other), abs(self))

    def __sub__(self, other):
        """
            a - b == a + (-b)
        """
        return self.__add__(-other)

    def __mul__(self, other):
        """
            Method returns the result of self * other.
        """

        if self.getBase() != other.getBase():
            raise BaseError()

        resultSize = self.getSize() + other.getSize() - 1;
        resultDigits = [0 for i in range(0, resultSize)]
        resultBase = self.getBase()

        for i, x in enumerate(self.getDigits()):
            for j, y in enumerate(other.getDigits()):
                resultDigits[i+j] += x * y

        carry = 0
        for i in range(0, resultSize):
            resultDigits[i] += carry

            carry = resultDigits[i] // resultBase
            resultDigits[i] %= resultBase

        if carry:
            resultDigits.append(carry)

        while len(resultDigits) > 1 and resultDigits[-1] == 0:
            resultDigits.pop()

        resultValue = ''.join([digitToSymbol[x] for x in resultDigits[::-1]])

        if self.getSign() != other.getSign():
            resultValue = '-' + resultValue

        return Number(resultValue, self.getBase())

    def integerDivision(self, a, b):
        """
            Method returns a tuple (quotient, remainder) representing
            the result of the integer division a / b.

            Note: <a> and <b> should be in the same base
                  <b> not zero.
        """

        if b == Number('0', b.getBase()):
            raise ZeroDivisionError()

        if a.getBase() != b.getBase():
            raise BaseError()

        quotientDigits = []
        rem = Number('0', a.getBase())
        for i in abs(a).getValue():
            rem *= Number('10', rem.getBase())
            rem += Number(i, rem.getBase())

            quotientDigits.append(0)

            while abs(b) <= abs(rem):
                quotientDigits[-1] += 1
                rem -= abs(b)

        quotientDigits = quotientDigits[::-1]
        while len(quotientDigits) > 1 and quotientDigits[-1] == 0:
            quotientDigits.pop()

        quotientValue = ''.join([digitToSymbol[digit] for digit in quotientDigits[::-1]])

        quotient = Number(quotientValue, a.getBase())

        if a.getSign() != b.getSign():
            quotient = -quotient
            quotient -= Number('1', quotient.getBase())

        rem = a - b * quotient
        return (quotient, rem)
