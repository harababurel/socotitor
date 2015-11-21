from tests.test import *
from models.number import *
from utils.random import *

# Test().testEverything()

# x = Number('-5')
# y = Number('1010110110', 2)
# z = Number('12AB', 16)

u = randomNumber(base=10)
v = randomNumber(base=10)

a = int(u.getValue())
b = int(v.getValue())


print(u.getValue())
print(a)
print()

print(v.getValue())
print(b)
print()

print((u*v).getValue())
print(a*b)

assert (u*v).getValue() == str(a*b)

# print(x)
# print(y)
