"""
    Some custom-made exceptions that are raised throughout the program.
"""

class BaseError(Exception):
    def __init__(self, message=None):
        if message is not None:
            self.__message = message
        else:
            self.__message = "Can't operate on numbers with different bases."

    def __str__(self):
        return self.__message

class DigitError(Exception):
    def __init__(self, message=None):
        if message is not None:
            self.__message = message
        else:
            self.__message = "The digits do not belong to the base."

    def __str__(self):
        return self.__message

class SignError(Exception):
    def __init__(self, message=None):
        if message is not None:
            self.__message = message
        else:
            self.__message = "Can't operate on numbers with this sign."

    def __str__(self):
        return self.__message

class ComparisonError(Exception):
    def __init__(self, message=None):
        if message is not None:
            self.__message = message
        else:
            self.__message = "Numbers do not have the right sizes."

    def __str__(self):
        return self.__message
