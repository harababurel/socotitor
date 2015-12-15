Project Summary
===============


Statement
---------

Socotitor is a Python application that is capable of operating arithmetically on integers represented in arbitrary numeration bases.

Operations
----------

The implemented operations are:
    * addition
    * subtraction
    * multiplication
    * integer division (quotient + remainder)
    * exponentiation

For each operation, both operands must be represented in the same base (2, 3, ..., 10, 16). If not, than one of them must first be converted to the other base.

Conversions
-----------

Socotitor implements three methods of converting bases:
    * substitution method
    * successive divisions
    * rapid conversions

The best of the three methods is chosen automatically by the application, depending on the bases of the conversion.

Expressions
-----------

Moreover, some more complex expressions can be evaluated. These allow using operands written in different bases. In addition, parantheses are allowed for specifying the priority of an operation.
