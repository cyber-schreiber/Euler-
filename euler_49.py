"""
Contains code for Project Euler problem 49:

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways:
(i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property,
but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""


def get_prime(n):
    """Returns True if n is prime, else False.
    Works in this code for primes less than or equal to 997661

    @type n: int
    @rtype: bool
    """
    for num in primes:
        if n % num == 0:
            return False
        if num > n / 2:
            return True

    return True

primes = [2]
iterator = 3

while iterator < 10000:

    if get_prime(iterator):
        primes.append(iterator)

    iterator += 1

print(primes)

four_digit = primes.index(997) + 1

for prime in primes[four_digit:]:
    for i in range(len(primes)-primes.index(prime)-1):
        next_prime = primes[primes.index(prime)+i+1]
        delta = next_prime - prime
        final = next_prime + delta
        if final in primes:
            first = [int(str(prime)[0]), int(str(prime)[1]), int(str(prime)[2]), int(str(prime)[3])]
            middle = [int(str(next_prime)[0]), int(str(next_prime)[1]),
                      int(str(next_prime)[2]), int(str(next_prime)[3])]
            last = [int(str(final)[0]), int(str(final)[1]), int(str(final)[2]), int(str(final)[3])]
            first.sort()
            middle.sort()
            last.sort()
            if first == middle == last:
                print(prime, next_prime, final)

