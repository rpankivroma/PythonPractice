"""
Exercise: 19: Print Alternate Prime Numbers till 20
A Prime Number is a number that can only be divided by itself and 1 without remainders (e.g., 2, 3, 5, 7, 11).

For example:

All prime numbers from 1 to 20: 2, 3, 5, 7, 11, 13, 17, 19

Alternate prime numbers from 1 to 20:
2, 5, 11, 17
"""

# Answer

import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    # Перевіряємо дільники до sqrt(n)
    limit = int(math.sqrt(n))
    for d in range(3, limit + 1, 2):
        if n % d == 0:
            return False
    return True

primes = [x for x in range(1, 21) if is_prime(x)]
print("All prime numbers from 1 to 20:", primes)

alternate_primes = primes[0::2]
print("Alternate prime numbers from 1 to 20:")
print(", ".join(str(x) for x in alternate_primes))

# Terminal output
#  PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe c:/Users/trade/Desktop/PythonPractice/PythonPractice/PyNative/Exercice_19.py
# All prime numbers from 1 to 20: [2, 3, 5, 7, 11, 13, 17, 19]
# Alternate prime numbers from 1 to 20:
# 2, 5, 11, 17