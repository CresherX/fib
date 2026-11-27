import math
from math import isqrt
f0 = 0
f1 = 1
fn = 0
massive_fib = []
def is_fib(n):
    if n > 0:
        x1 = math.sqrt(5*n**2 + 4)
        x2 = math.sqrt(5*n**2 - 4)
        if  x1.is_integer() or x2.is_integer():
            return True
        else:
            return False
for i in range(1, 100):
    fn = f0 + f1
    f0 = f1
    f1 = fn