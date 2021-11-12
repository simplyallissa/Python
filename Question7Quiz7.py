# Allissa Hertz
# Nov. 3, 2021
# input, n
# output: prime or not

import math

i = 2
is_prime = True


n = int(input("Enter a number: "))

if n < 2:
    raise ValueError("Must be a number > 2")

while i < math.isqrt(n):
    print(n % i)
    if n % i == 0:
        is_prime = False
        break
    i += 1
    
if is_prime:
    print(f"{n} is prime")
else:
    print(f"{n} is not prime")
    
    
