from tests.test import *
from models.number import *
from utils.random import *

# Test().testEverything()

# x = Number('-5')
# y = Number('1010110110', 2)
# z = Number('12AB', 16)

u = randomNumber(size=10, base=10)
v = randomNumber(size=4, base=10)

a = int(u.getValue())
b = int(v.getValue())


print(' u  = ' + u.getValue())
print('|u| = ' + abs(u).getValue())
print(' a  = ' + str(a))
print()

print(' v  = ' + v.getValue())
print('|v| = ' + abs(v).getValue())
print(' b  = ' + str(b))
print()


quotient = u//v
remainder = u%v

print("DIVISION:")
print(quotient.getValue(), remainder.getValue())
print(a//b, a%b)

assert (a//b) * b + (a%b) == a
assert quotient * v + remainder == u
print()

print("ADDITION/SUBTRACTION:")
print((u+v).getValue() + " should be " + str(a+b))
print((u-v).getValue() + " should be " + str(a-b))

