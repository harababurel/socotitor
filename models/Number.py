"""
    Module implements the Number class.
"""
from models.Exceptions import *

class Number:
    """
        The Number class models an integer value in some base.
    """

    def __init__(self, value, base=10):
        """
            If not provided, the base is considered to be 10.
        """
        self.__base = base
        self.__value = str(value)
        self.__size = len(self.__value)

    def __repr__(self):
        return "%s(%s)" % (self.__value, self.__base)

    def getBase(self):
        return self.__base

    def getValue(self):
        return self.__value

    def __add__(self, other):
        """
            Method returns the result of self + other.
        """

        if self.getBase() != other.getBase():
            raise BaseError()

        return "TODO: add numbers"

