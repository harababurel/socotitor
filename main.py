from tests.test import *
from models.number import *
from utils.random import *

# Test().testEverything()

# x = Number('-5')
# y = Number('1010110110', 2)
# z = Number('12AB', 16)

u = randomNumber(sign=1, size=3, base=10)
v = randomNumber(sign=0, size=3, base=10)

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

print((u+v).getValue())
print(a+b)
