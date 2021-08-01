from math import sqrt
from itertools import count, islice


def is_prime(n):
    if n < 2:
        return False

    for number in islice(count(2), int(sqrt(n) - 1)):
        if n % number == 0:
            return False

    return True


x = int(input())
Arr = []
for i in range(x):
    Arr.append(int(input()))

for y in Arr:
    if is_prime(y):
        print("Prime")
    else:
        print("Not prime")
